# Sources, credits & independence

This work assembles a **new nanoDNS configuration** informed by public community research. It is **not** a verbatim redistribution of someone else's hosts file and does not bundle third-party executables. DNS names are factual indicators; source descriptions, code and licensing remain with their original authors.

## nanoDNS — core runtime

- **[Drakmor / nanoDNS](https://github.com/drakmor/nanoDNS)** — upstream payload, INI syntax, UDP DNS behavior, wildcard matching, `MAX_RULES=128`, local IPv4/IPv6 listeners. **Independent project**; this repository is not maintained or endorsed by Drakmor.

## PlayStation and cross-console research

- **[Al-Azif / dns-config-watchdog](https://github.com/Al-Azif/dns-config-watchdog)** — historical PlayStation and Nintendo DNS zone data.
- **[MagicStuffCL / DnsblockListPS4PS5_Adguardhome](https://github.com/MagicStuffCL/DnsblockListPS4PS5_Adguardhome)** — PS4/PS5 blocking indicators.
- **[cjrb007 / ps5-dns-block](https://github.com/cjrb007/ps5-dns-block)** — PS5 firmware/update/CDN hostnames; credits MODDED WARFARE, CasperMcFadden95 and Al-Azif.
- **[Misl3d / PS-dns-block](https://github.com/Misl3d/PS-dns-block)** — PS4 and PS5 public combined indicator list (references phoanglong/cjrb007).
- **[ZixX3r / Console-DNS-Block](https://github.com/ZixX3r/Console-DNS-Block)** — Nintendo Switch/Wii U and Microsoft/EA research.
- **[b0bfranklin / Playstation_Blocklists](https://github.com/b0bfranklin/Playstation_Blocklists)** — PS5 blocklist examples.
- **[NukelordPvP / block-console-servers](https://github.com/NukelordPvP/block-console-servers)** — firmware and telemetry host reference lists.
- **[baddump / ps5-block-dns](https://github.com/baddump/ps5-block-dns)** — independently compiled PS5 update list.

Public community discussions (e.g. PS4 homebrew and PSN DNS traces) also informed the deliberate inclusion of `a192.d.akamai.net`. Because its CDN operator is shared, it is documented as an **intentional false-positive risk** rather than guaranteed Sony-only infrastructure.

## Evidence classification

1. **Observed:** PS5 nanoDNS v0.4 runtime log from 10 October 2026, showing successful startup and actual Sony-domain override responses.
2. **Static tests:** selected representative hostnames match or do not match our wildcard policy.
3. **Community references:** older or newer published endpoints included for coverage, **without claiming their production status is verified today**.

This repository does **not** publish the user-provided full console log because it may contain local device information and because it would be misleading to treat one session as a complete capture.

## Licensing and attribution

The repository's original organization, documentation and validation scripts are offered under its existing **GPL-3.0** [LICENSE](../LICENSE). Linked source projects and any quoted extracts retain their own copyrights and licenses. Do not assume this repository relicenses their software. If a contribution reproduces external code, check its license and preserve required attribution.

Names and trademarks of Sony, PlayStation, Nintendo, Xbox, Microsoft, Electronic Arts, Epic Games and others belong to their respective owners. Mention does not imply affiliation or endorsement.
