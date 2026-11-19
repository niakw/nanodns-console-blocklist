# Coverage, evidence & verification

> **Scope:** A list of known or brand-matched **DNS hostnames**. Platform branding does not imply complete coverage of every online service.

| Family | Current coverage approach | Hardware verification |
| --- | --- | --- |
| platform operator / platform network / console / target consoles | Brand masks plus SIE, platform network and shared CDN provider-specific names | **console 13.60: observed platform operator queries blocked**, not exhaustive |
| other console ecosystem (legacy/legacy console/3DS/legacy console U/legacy console/legacy console 2) | Brand masks and `legacy console.com` family | Static matching only |
| other console ecosystem / 360 / One / Series | other console ecosystem-branded domains, other console ecosystem Live/Services, selected CDN names | Static matching only |
| game publisher / game publisher / Take-Two / game publisher | Core publisher brands and service domains | Static matching only |
| game publisher / game publisher / game publisher / CD Projekt / game publisher | Selected families and brand subdomains | Static matching only |
| game publisher / game publisher / Square Enix / game publisher game publisher | Selected brand families | Static matching only |

## Current resolver policy versus historic console proof

The repository now configures only Quad9's secure IPv4 resolver pair (`9.9.9.9`, `149.112.112.112`) for authorized names. The observations below were captured **before** this change; they do not prove current resolver fallback or the new configuration has been tested on console.

## What the console log showed (10 October 2026)

A user-provided nanoDNS v0.4 startup/operation log showed:

- `124 rule(s)`, `0 exception(s)`, two upstreams and listeners on IPv4 `127.0.0.1:53` and IPv6 `[::1]:53`;
- platform operator/platform services DNS names such as `<hostname-or-mask-from-the-INI>`, `<hostname-or-mask-from-the-INI>`, `<hostname-or-mask-from-the-INI>`, `<hostname-or-mask-from-the-INI>` and `<hostname-or-mask-from-the-INI>` matched local override rules;
- queried A records returned `0.0.0.0`, while matching AAAA queries returned `NOERROR` with **zero answers**;
- many repeated queries for `<hostname-or-mask-from-the-INI>`.

This is useful evidence that **observed DNS lookups** were intercepted. It is **not** evidence that no unlisted names resolve, all upstream Internet access works, or firmware updating is impossible. No full packet-capture or end-to-end update attempt was performed.

## Installation vs. observed coverage

The sequence matters: seeing a startup log **before** changing console DNS does not prove the console is using nanoDNS. Confirm a subsequent `query from=127.0.0.1`, `override matched`, and the expected blocked A / AAAA response in the **current** nanoDNS session. After a full reboot, check again. A public Internet connection may be re-enabled only if the user accepts that DNS-only filtering does **not** prevent direct-IP, alternate-resolver or pre-payload traffic.

See [safe install (English)](INSTALL.md), [installation sécurisée (français)](INSTALL.fr.md) and [startup risk model](SETUP_SAFETY.md).

## Checking rules locally

Run without third-party Python dependencies:

```bash
python3 -m unittest discover -s tests -v
```

Tests enforce a 124-rule baseline, no duplicate masks, no enabled exceptions, no global all-domain rule, and representative negative controls (`github.com`, `youtube.com`, etc.). Matching tests approximate the current wildcard subset used by this file; native behavior is determined by nanoDNS.

## Reporting missing domains

Please include the exact hostname, platform, whether the name is an observed console query or documentation-only, source link, expected DNS action, false-positive risk and reproduction steps. Sanitise public logs: they may contain local addresses, timestamps and user-identifying hostnames.

**Known limitation:** broad `<hostname-or-mask-from-the-INI>` and `<hostname-or-mask-from-the-INI>` can match domains unrelated to these vendors. `<hostname-or-mask-from-the-INI>` is shared infrastructure. If you encounter a breakage, do not assume the provider is malicious; propose the narrowest adjustment supported by evidence.
