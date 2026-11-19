# Sources, credits & independence

This work assembles a **new nanoDNS configuration** informed by public community research. It is **not** a verbatim redistribution of someone else's hosts file and does not bundle third-party executables. DNS names are factual indicators; source descriptions, code and licensing remain with their original authors.

## nanoDNS — core runtime

- **[Drakmor / nanoDNS](https://github.com/drakmor/nanoDNS)** — upstream payload, INI syntax, UDP DNS behavior, wildcard matching, `MAX_RULES=128`, local IPv4/IPv6 listeners. **Independent project**; this repository is not maintained or endorsed by Drakmor.

## DNS upstream provider

- **[Quad9 recommended secure resolvers](https://quad9.net/service/service-addresses-and-features/)** — source for the `9.9.9.9` and `149.112.112.112` pair, malware blocking and DNSSEC validation. Both are addresses of the same operator, not independent upstream providers. The plain nanoDNS UDP transport is not encrypted.

## platform services and cross-console research

- **[Al-Azif / dns-config-watchdog](https://github.com/Al-Azif/dns-config-watchdog)** — historical platform services and other console ecosystem DNS zone data.
- **[MagicStuffCL / DnsblockListPS4PS5_Adguardhome](https://github.com/MagicStuffCL/DnsblockListPS4PS5_Adguardhome)** — target consoles blocking indicators.
- **[cjrb007 / console-dns-block](https://github.com/cjrb007/ps5-dns-block)** — console firmware/update/CDN hostnames; credits MODDED WARFARE, CasperMcFadden95 and Al-Azif.
- **[Misl3d / PS-dns-block](https://github.com/Misl3d/PS-dns-block)** — console and console public combined indicator list (references phoanglong/cjrb007).
- **[ZixX3r / Console-DNS-Block](https://github.com/ZixX3r/Console-DNS-Block)** — other console ecosystem legacy console/legacy console U and platform operator/game publisher research.
- **[b0bfranklin / Playstation_Blocklists](https://github.com/b0bfranklin/Playstation_Blocklists)** — console blocklist examples.
- **[NukelordPvP / block-console-servers](https://github.com/NukelordPvP/block-console-servers)** — firmware and telemetry host reference lists.
- **[baddump / console-block-dns](https://github.com/baddump/ps5-block-dns)** — independently compiled console update list.

Public community discussions (e.g. console homebrew and platform network DNS traces) also informed the deliberate inclusion of `<hostname-or-mask-from-the-INI>`. Because its CDN operator is shared, it is documented as an **intentional false-positive risk** rather than guaranteed platform operator-only infrastructure.

## Evidence classification

1. **Observed:** console nanoDNS v0.4 runtime log from 10 October 2026, showing successful startup and actual platform operator-domain override responses.
2. **Static tests:** selected representative hostnames match or do not match our wildcard policy.
3. **Community references:** older or newer published endpoints included for coverage, **without claiming their production status is verified today**.

This repository does **not** publish the user-provided full console log because it may contain local device information and because it would be misleading to treat one session as a complete capture.

## Licensing and attribution

The repository's original organization, documentation and validation scripts are offered under its existing **GPL-3.0** [LICENSE](../LICENSE). Linked source projects and any quoted extracts retain their own copyrights and licenses. Do not assume this repository relicenses their software. If a contribution reproduces external code, check its license and preserve required attribution.

Names and trademarks of platform operator, platform services, other console ecosystem, other console ecosystem, platform operator, Electronic Arts, game publisher and others belong to their respective owners. Mention does not imply affiliation or endorsement.
