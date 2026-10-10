# Coverage, evidence & verification

> **Scope:** A list of known or brand-matched **DNS hostnames**. Platform branding does not imply complete coverage of every online service.

| Family | Current coverage approach | Hardware verification |
| --- | --- | --- |
| Sony / PSN / PS3 / PS4 / PS5 | Brand masks plus SIE, PSN and Akamai-specific names | **PS5 13.60: observed Sony queries blocked**, not exhaustive |
| Nintendo (legacy/Wii/3DS/Wii U/Switch/Switch 2) | Brand masks and `wii.com` family | Static matching only |
| Xbox / 360 / One / Series | Xbox-branded domains, Xbox Live/Services, selected CDN names | Static matching only |
| Epic / Rockstar / Take-Two / 2K | Core publisher brands and service domains | Static matching only |
| EA / Ubisoft / Sega / CD Projekt / GOG | Selected families and brand subdomains | Static matching only |
| Valve / Capcom / Square Enix / Bandai Namco | Selected brand families | Static matching only |

## What the PS5 log showed (10 October 2026)

A user-provided nanoDNS v0.4 startup/operation log showed:

- `124 rule(s)`, `0 exception(s)`, two upstreams and listeners on IPv4 `127.0.0.1:53` and IPv6 `[::1]:53`;
- Sony/PlayStation DNS names such as `ps5.np.playstation.net`, `fuk01.ps5.update.playstation.net`, `ena.net.playstation.net`, `telemetry-console.api.playstation.com` and `smetrics.aem.playstation.com` matched local override rules;
- queried A records returned `0.0.0.0`, while matching AAAA queries returned `NOERROR` with **zero answers**;
- many repeated queries for `ps5.np.playstation.net`.

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

**Known limitation:** broad `*sony*` and `*nintendo*` can match domains unrelated to these vendors. `a192.d.akamai.net` is shared infrastructure. If you encounter a breakage, do not assume the provider is malicious; propose the narrowest adjustment supported by evidence.
