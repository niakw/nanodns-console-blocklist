"""Documentation contracts: neutral display, complete bilingual entry points and links."""
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
BRANDS=re.compile(r"\b(?:sony|nintendo|playstation|xbox|microsoft|epic|rockstar|ubisoft|sega|cloudflare|google|capcom|bandai|namco|steam|valve|gog|psn|ps4|ps5|ps3|akamai|electronic arts|take.two|square enix|cd projekt)\b",re.I)
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
   for term in ("124","Quad9","Drakmor"):
    self.assertIn(term,s)

 def test_no_visible_vendor_marking(self):
  for file in ROOT.rglob("*.md"):
   s=file.read_text(encoding="utf-8")
   s=re.sub(r"\]\([^)]*\)","]()",s)
   s=re.sub(r"https?://[^\s)>]+","",s)
   match=BRANDS.search(s)
   self.assertIsNone(match, f"{file.relative_to(ROOT)}: {match.group(0) if match else ''}")

 def test_internal_markdown_links(self):
  for file in ROOT.rglob("*.md"):
   for link in re.findall(r"\]\(([^)]+)\)",file.read_text(encoding="utf-8")):
    if link.startswith(("http:","https:","#","mailto:")):continue
    path=link.split("#",1)[0].split("?",1)[0]
    if not path:continue
    with self.subTest(file=str(file.relative_to(ROOT)),link=link):
     self.assertTrue((file.parent/path).is_file())
