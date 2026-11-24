"""Documentation contracts: neutral display, complete bilingual entry points and links."""
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
BRANDS=re.compile(r"\b(?:sony|nintendo|playstation|xbox|microsoft|epic|rockstar|ubisoft|sega|cloudflare|google|capcom|bandai|namco|steam|valve|gog|psn|ps4|ps5|ps3|akamai|electronic arts|take.two|square enix|cd projekt|dualsense|sie|wii|switch)\b",re.I)
PAIRS=(
 ("README.md","README.fr.md"),
 ("docs/INSTALL.md","docs/INSTALL.fr.md"),
 ("docs/COMPARISON.md","docs/COMPARISON.fr.md"),
 ("docs/COVERAGE.md","docs/COVERAGE.fr.md"),
 ("docs/SOURCES.md","docs/SOURCES.fr.md"),
 ("docs/THREAT_MODEL.md","docs/THREAT_MODEL.fr.md"),
 ("docs/SETUP_SAFETY.md","docs/SETUP_SAFETY.fr.md"),
 ("SECURITY.md","SECURITY.fr.md"),
 ("CONTRIBUTING.md","CONTRIBUTING.fr.md"),
 ("CHANGELOG.md","CHANGELOG.fr.md"),
)

class PresentationContract(unittest.TestCase):
 def test_english_and_french_pairs(self):
  for en,fr in PAIRS:
   with self.subTest(en=en):
    a=ROOT/en;b=ROOT/fr
    self.assertTrue(a.is_file());self.assertTrue(b.is_file())
    self.assertIn(b.name,a.read_text(encoding="utf-8"))
    self.assertIn(a.name,b.read_text(encoding="utf-8"))

 def test_english_default_install_target(self):
  en=(ROOT/"README.md").read_text(encoding="utf-8")
  self.assertIn("(docs/INSTALL.md)",en)
  self.assertIn("(docs/INSTALL.fr.md)",en)
  self.assertLess(en.index("(docs/INSTALL.md)"),en.index("(docs/INSTALL.fr.md)"))
  for s in (en,(ROOT/"README.fr.md").read_text(encoding="utf-8")):
   for term in ("124","Control D","Drakmor"):
    self.assertIn(term,s)

 def test_no_visible_vendor_marking(self):
  # The specific firmware target is necessary when presenting our tested
  # nanoDNS 13.60 alternative. Do not permit other vendor names globally.
  runtime_docs={
   "README.md", "README.fr.md",
   "docs/COMPARISON.md", "docs/COMPARISON.fr.md",
   "CHANGELOG.md", "CHANGELOG.fr.md"
  }
  for file in ROOT.rglob("*.md"):
   s=file.read_text(encoding="utf-8")
   s=re.sub(r"\]\([^)]*\)","]()",s)
   s=re.sub(r"https?://[^\s)>]+","",s)
   rel=file.relative_to(ROOT).as_posix()
   permitted={"ps5","ps4"} if rel in runtime_docs else set()
   match=next((m for m in BRANDS.finditer(s) if m.group(0).lower() not in permitted),None)
   self.assertIsNone(match, f"{rel}: {match.group(0) if match else ''}")

 def test_firmware_specific_runtime_recommendation(self):
  expected="https://github.com/niakw/nanoDNS-Encore"
  for path in ("README.md","README.fr.md","docs/COMPARISON.md","docs/COMPARISON.fr.md"):
   s=(ROOT/path).read_text(encoding="utf-8")
   with self.subTest(file=path):
    self.assertIn(expected,s)
    self.assertIn("13.60",s)
    self.assertIn("PS5",s)
    self.assertIn("0.4-13.60.2",s)
  en=(ROOT/"README.md").read_text(encoding="utf-8")
  fr=(ROOT/"README.fr.md").read_text(encoding="utf-8")
  self.assertIn("Other PS5 firmwares and PS4 have not been user-validated",en)
  self.assertIn("Les autres firmwares PS5 et la PS4 ne sont pas validés",fr)

 def test_internal_markdown_links(self):
  for file in ROOT.rglob("*.md"):
   for link in re.findall(r"\]\(([^)]+)\)",file.read_text(encoding="utf-8")):
    if link.startswith(("http:","https:","#","mailto:")):continue
    path=link.split("#",1)[0].split("?",1)[0]
    if not path:continue
    with self.subTest(file=str(file.relative_to(ROOT)),link=link):
     self.assertTrue((file.parent/path).is_file())
