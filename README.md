<div align="center">

# nanoDNS Console Blocklist

### Block console service DNS. Keep the rest of your Internet.

**A selective, multi-generation DNS denylist for PS4 / PS5 homebrew and emulation environments.**

[![nanoDNS](https://img.shields.io/badge/payload-nanoDNS%20v0.4-8250df)](https://github.com/drakmor/nanoDNS)
![PS4 / PS5](https://img.shields.io/badge/target-PS4%20%2F%20PS5-3558a6)
![Rules](https://img.shields.io/badge/selective%20rules-124-6f42c1)
![Exceptions](https://img.shields.io/badge/exceptions-0-2ea44f)
[![License: GPL-3.0](https://img.shields.io/badge/license-GPL--3.0-blue)](LICENSE)
[![Status](https://img.shields.io/badge/status-community%20beta-orange)](CHANGELOG.md)

**PlayStation · Nintendo · Xbox · Game Publishers · Emulator-aware DNS filtering**

[**Get the configuration**](nanodns.ini) · [**Install guide**](docs/INSTALL.md) · [**Coverage**](docs/COVERAGE.md) · [**Security model**](docs/THREAT_MODEL.md)

</div>

---

## One console. Multiple generations. One selective DNS policy.

A modded PS5 can host far more than one PlayStation experience: homebrew tools, emulators and game-related applications may attempt to resolve endpoints belonging to **PlayStation, Nintendo, Xbox and individual publishers**. Default console DNS settings do not distinguish between a harmless media request and a game-service request.

**nanoDNS Console Blocklist gives you that distinction at the DNS layer.** It supplies a readable `nanodns.ini` profile that tells [Drakmor's nanoDNS](https://github.com/drakmor/nanoDNS) which known console and publisher names to answer locally—while forwarding **unlisted** DNS names to ordinary upstream resolvers.

This is **not** the crude “disconnect everything” approach. It is selective DNS filtering intended for people who want more control over a console's network behavior **without intentionally shutting down unrelated Internet access**.

> [!IMPORTANT]
> **DNS filtering is not a firewall, a firmware-update guarantee or a complete security boundary.** This list only affects queries handled by a running nanoDNS instance. Cached addresses, direct-IP connections, alternate DNS/DoH, DNS over TCP, traffic before payload startup and undiscovered domains can bypass this list. See the [threat model](docs/THREAT_MODEL.md).

## Why this project?

| | Stock DNS / public resolver | Global DNS kill switch | **Console Blocklist + nanoDNS** |
| --- | --- | --- | --- |
| Known PlayStation service names | Usually resolve | No DNS | **Filtered** |
| Known Nintendo & Xbox names | Usually resolve | No DNS | **Filtered** |
| Selected game publishers | Usually resolve | No DNS | **Filtered** |
| Unrelated domains (e.g. GitHub) | Resolve | **Blocked** | **Forwarded to upstream** |
| Runs on console via nanoDNS | No | Depends | **Yes, while payload runs** |
| Protects against direct-IP connections | No | No | **No** |

### Built for the emulator era

- **PS4 + PS5 first:** firmware-update endpoints, PSN-linked names, telemetry, service APIs and historically documented PlayStation delivery aliases.
- **Nintendo across generations:** branded Wii, DS/3DS, Wii U, Switch and Switch 2 service hostnames, plus legacy Wii endpoints.
- **Xbox across generations:** Xbox Live, Xbox Network, Game Pass, legacy Xbox 360-style families and selected Microsoft/CDN aliases.
- **Publisher-aware:** Epic, Rockstar/Take-Two/2K, EA, Ubisoft, Sega, CD Projekt/GOG, Steam/Valve, Capcom, Square Enix and Bandai Namco.
- **Predictable configuration:** **124 explicit override rules, zero exceptions**, and two upstreams for *unlisted* domains.
- **Auditable and open:** plain-text policy, public sources, automated static validation, and community contributions.

> **Compatibility note:** Covering names associated with a platform does **not** prove that all of its online services, games or emulators are isolated. This project is designed to reduce selected DNS exposure; it does not modify emulator network stacks or game code.

## Install in three steps

1. Install and start the compatible [nanoDNS payload](https://github.com/drakmor/nanoDNS) on your own PS4/PS5 homebrew environment.
2. Download [`nanodns.ini`](nanodns.ini) and copy it to **`/data/nanodns/nanodns.ini`** (back up your previous file first). Restart the payload to load the new rules.
3. Set **both console DNS fields to `127.0.0.1`**, matching `bind=127.0.0.1`, and inspect `/data/nanodns/nanodns.log` for loading, blocked queries and upstream forwarding.

**Do not put a public resolver as the console's secondary DNS**; it can bypass the local filter. The `1.1.1.1` and `9.9.9.9` entries **inside** nanoDNS are used only for names without an override.

Full instructions, recovery steps and troubleshooting: [Installation Guide](docs/INSTALL.md).

```ini
[general]
bind=127.0.0.1
bind6=::1

[upstream]
server=1.1.1.1
server=9.9.9.9

[overrides]
*playstation*=0.0.0.0
*nintendo*=0.0.0.0
*.xboxlive.com=0.0.0.0
# ... 121 more carefully grouped rules

[exceptions]
# None
```

## What has actually been verified?

**Observed on PS5 firmware 13.60 with nanoDNS v0.4 (10 October 2026):** the payload loaded **124 rules / 0 exceptions**, bound UDP DNS on `127.0.0.1:53` and `[::1]:53`, and returned `0.0.0.0` (A) / no answer (AAAA) for the **Sony/PlayStation domains present in the supplied device log**.

**Not verified on hardware:** that *all* network traffic is blocked for every supported ecosystem; full coverage of Nintendo, Xbox and publishers; resistance to direct-IP requests; behavior before the payload starts; and the continued availability of every nonlisted website.

**Static tests** check configuration integrity and representative blocked/allowed domains. They are **not a network penetration test** or a guarantee about future endpoints. See [Coverage & Validation](docs/COVERAGE.md).

## Know the trade-offs

Broad masks such as `*sony*`, `*playstation*` and `*nintendo*` can block unrelated domains containing those strings. The exact name `a192.d.akamai.net` is included intentionally because it appears in historical PlayStation update traces, but Akamai is a **shared CDN** and collateral blocking is possible. Publisher-wide masks also remove legitimate online functions.

This project does **not** ship an exploit, an emulator, a game, a payload, any copyrighted game content or any software to bypass a service's authentication.

## Project files

| File | Purpose |
| --- | --- |
| [`nanodns.ini`](nanodns.ini) | **Installable selective policy** |
| [`docs/INSTALL.md`](docs/INSTALL.md) | Installation, logging, recovery |
| [`docs/COVERAGE.md`](docs/COVERAGE.md) | Platforms, expected effects, validation status |
| [`docs/THREAT_MODEL.md`](docs/THREAT_MODEL.md) | Explicit protections and bypasses |
| [`docs/SOURCES.md`](docs/SOURCES.md) | Community research, attribution, data provenance |
| [`tests/test_config.py`](tests/test_config.py) | Offline unit tests |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to suggest a domain and evidence |
| [`SECURITY.md`](SECURITY.md) | Responsible reporting |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |

## Credits & community

**nanoDNS is made by [Drakmor](https://github.com/drakmor/nanoDNS).** This repository provides a separate, community-maintained **configuration**, not a fork or official distribution of that payload.

Research and publicly documented hostnames were compared against [Al-Azif](https://github.com/Al-Azif/dns-config-watchdog), [MagicStuffCL](https://github.com/MagicStuffCL/DnsblockListPS4PS5_Adguardhome), [cjrb007](https://github.com/cjrb007/ps5-dns-block), [Misl3d](https://github.com/Misl3d/PS-dns-block), [ZixX3r](https://github.com/ZixX3r/Console-DNS-Block) and other sources credited in [SOURCES.md](docs/SOURCES.md). Their original projects remain independent and subject to their own licenses.

**Made for the console homebrew and emulation community, with transparency before promises.** Contributions and reproducible test results are welcome.

---

<div align="center"><sub>Independent community project · Not affiliated with Sony, Nintendo, Microsoft, Drakmor, or any game publisher · GPL-3.0</sub></div>
