"""Document safety contract: prevent accidental removal of critical install steps."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SafeInstallDocumentation(unittest.TestCase):
    def test_both_languages_and_readme_linked(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for path in ("docs/INSTALL.md", "docs/INSTALL.fr.md", "docs/SETUP_SAFETY.md"):
            self.assertTrue((ROOT / path).is_file(), path)
        self.assertIn("(docs/INSTALL.md)", readme)
        self.assertIn("(docs/INSTALL.fr.md)", readme)
        self.assertIn("(docs/SETUP_SAFETY.md)", readme)

    def test_quad9_only_upstreams_and_bilingual_examples(self):
        ini = (ROOT / "nanodns.ini").read_text(encoding="utf-8")
        en = (ROOT / "docs/INSTALL.md").read_text(encoding="utf-8")
        fr = (ROOT / "docs/INSTALL.fr.md").read_text(encoding="utf-8")
        for document in (ini, en, fr):
            self.assertIn("server=9.9.9.9", document)
            self.assertIn("server=149.112.112.112", document)
            self.assertNotIn("server=1.1.1.1", document)
            self.assertNotIn("server=8.8.8.8", document)
        self.assertIn("README.fr.md", (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertTrue((ROOT / "README.fr.md").is_file())

    def test_en_complete_safe_order(self):
        s = (ROOT / "docs/INSTALL.md").read_text(encoding="utf-8")
        gates = (
            "WAN still denied", "nanodns.ini.bak", "/data/nanodns/nanodns.ini",
            "restart the nanoDNS payload", "First log gate", "124 rule(s)",
            "0 exception(s)", "Primary DNS", "Secondary DNS", "127.0.0.1",
            "Confirm actual DNS interception", "Optional controlled WAN return",
            "After every reboot", "Recovery / failure scenarios", "direct-IP",
        )
        for gate in gates:
            with self.subTest(gate=gate):
                self.assertIn(gate, s)
        self.assertLess(s.index("First log gate"), s.index("Configure BOTH console DNS fields"))
        self.assertLess(s.index("Configure BOTH console DNS fields"), s.index("Confirm actual DNS interception"))
        self.assertLess(s.index("Confirm actual DNS interception"), s.index("Optional controlled WAN return"))

    def test_fr_complete_safe_order(self):
        s = (ROOT / "docs/INSTALL.fr.md").read_text(encoding="utf-8")
        gates = (
            "WAN toujours bloqué", "nanodns.ini.bak", "/data/nanodns/nanodns.ini",
            "Premiers logs attendus", "124 rule(s)", "0 exception(s)",
            "DNS principal", "DNS secondaire", "127.0.0.1",
            "Revérifier les logs", "Réactiver éventuellement Internet",
            "Après un reboot", "Checklist finale", "connexion IP directe",
        )
        for gate in gates:
            with self.subTest(gate=gate):
                self.assertIn(gate, s)
        self.assertLess(s.index("Premiers logs attendus"), s.index("Modifier les DEUX champs DNS"))
        self.assertLess(s.index("Modifier les DEUX champs DNS"), s.index("Revérifier les logs"))
        self.assertLess(s.index("Revérifier les logs"), s.index("Réactiver éventuellement Internet"))


if __name__ == "__main__":
    unittest.main()
