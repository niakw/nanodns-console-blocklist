"""Offline configuration checks; no network queries and no PS5 access required."""
import fnmatch
import ipaddress
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = ROOT / "nanodns.ini"
LIMIT = 128


def config():
    sections = {}
    section = None
    for idx, original in enumerate(PATH.read_text(encoding="utf-8").splitlines(), 1):
        line = original.split("#", 1)[0].strip()
        if not line:
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1].lower()
            if section in sections:
                raise ValueError(f"Duplicate section {section} on line {idx}")
            sections[section] = []
            continue
        if section is None:
            raise ValueError(f"Orphan line {idx}")
        sections[section].append(line)
    return sections


def blocked(host, masks):
    # The shipped policy only uses exact names and '*' wildcards.
    # Python's fnmatchcase is equivalent for this subset of nanoDNS masks.
    host = host.lower().rstrip(".")
    return any(fnmatch.fnmatchcase(host, mask) for mask in masks)


class ConfigTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.parts = config()
        cls.overrides = cls.parts["overrides"]
        cls.rules = [line.split("=", 1) for line in cls.overrides]
        cls.masks = [mask.lower() for mask, _ in cls.rules]

    def test_expected_sections(self):
        self.assertEqual(set(self.parts), {"general", "upstream", "overrides", "exceptions"})

    def test_format_and_rule_cap(self):
        self.assertEqual(len(self.rules), 124, "review baseline changes explicitly")
        self.assertLessEqual(len(self.rules), LIMIT)
        self.assertEqual(len(set(self.masks)), len(self.masks))
        for mask, address in self.rules:
            self.assertTrue(mask and mask == mask.lower())
            self.assertNotIn(" ", mask)
            self.assertEqual(str(ipaddress.IPv4Address(address)), "0.0.0.0")
            self.assertTrue(re.fullmatch(r"[a-z0-9.*-]+", mask), mask)

    def test_no_global_block_or_exceptions(self):
        self.assertNotIn("*", self.masks)
        self.assertEqual(self.parts["exceptions"], [])
        self.assertFalse(blocked("github.com", self.masks))
        self.assertFalse(blocked("youtube.com", self.masks))
        self.assertFalse(blocked("google.com", self.masks))
        self.assertFalse(blocked("api.github.com", self.masks))
        self.assertFalse(blocked("raw.githubusercontent.com", self.masks))

    def test_loopback_only(self):
        self.assertIn("bind=127.0.0.1", self.parts["general"])
        self.assertIn("bind6=::1", self.parts["general"])
        self.assertIn("server=1.1.1.1", self.parts["upstream"])
        self.assertIn("server=9.9.9.9", self.parts["upstream"])

    def test_sony_representatives(self):
        for name in (
            "ps5.np.playstation.net", "telemetry-console.api.playstation.com",
            "fus01.ps5.update.playstation.net", "deu01.ps4.update.playstation.net",
            "fus01.ps3.update.playstation.net", "psn.akadns99.net",
            "a192.d.akamai.net", "us.np.stun.playstation.net",
            "ena.net.playstation.net", "feature.api.playstation.com",
        ):
            with self.subTest(name=name):
                self.assertTrue(blocked(name, self.masks))

    def test_multi_console_and_publishers(self):
        for name in (
            "atumn.hac.lp1.d4c.nintendo.net", "receive-us.dg.srv.nintendo.net",
            "www.nintendoswitch.com", "ctest.cdn.nintendo.net",
            "cfh.wapp.wii.com", "xsts.auth.xboxlive.com",
            "xblconfiggateway.xboxservices.com", "xboxlive.com.edgesuite.net",
            "accounts.epicgames.com", "telemetry.ea.com",
            "gog.com", "rsgameservices.com", "ubisoftconnect.com",
            "steampowered.com", "bandainamcoent.com",
        ):
            with self.subTest(name=name):
                self.assertTrue(blocked(name, self.masks))


if __name__ == "__main__":
    unittest.main()
