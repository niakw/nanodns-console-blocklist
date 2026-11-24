# Sources, licensing & provenance

**Language:** English (default) · [Français](SOURCES.fr.md)

This repository publishes a newly organized, auditable **configuration**, not a bundled executable and not a verbatim redistribution of third-party host files. Hostname indicators are compiled from publicly documented research and checks; code and documentation from other projects retain their own licenses.

## Original runtime

- [Drakmor / nanoDNS](https://github.com/drakmor/nanoDNS) — original payload, INI syntax, UDP DNS forwarding, wildcard behavior and local listeners. Our blocklist is **independent** and not an official release from its author.

## Protected DNS upstream

- [Control D free DNS](https://docs.controld.com/docs/free-dns) and [AdGuard public DNS](https://adguard-dns.io/en/public-dns.html) — unfiltered upstream addresses in configured order: `76.76.2.0`, `76.76.10.0`, `94.140.14.140`, `94.140.14.141`. [Quad9 withdrawal from France](https://quad9.net/news/blog/au-revoir-france/) prompted the 24 November 2026 migration.
- Both addresses belong to **one provider**. nanoDNS sends ordinary **unencrypted UDP** to its configured upstreams; the blocklist does not add DNS-over-TLS or DNS-over-HTTPS.

## Additional public community research

The following independent works informed historical hostnames, host-family patterns and false-positive reviews:

- [Al-Azif / dns-config-watchdog](https://github.com/Al-Azif/dns-config-watchdog) — historical service DNS research.
- [MagicStuffCL / community DNS list](https://github.com/MagicStuffCL/DnsblockListPS4PS5_Adguardhome) — community hostname indicators.
- [cjrb007 / community service DNS](https://github.com/cjrb007/ps5-dns-block) — update and delivery-name research.
- [Misl3d / community DNS list](https://github.com/Misl3d/PS-dns-block) — cross-generation hostname indicators.
- [ZixX3r / console DNS list](https://github.com/ZixX3r/Console-DNS-Block) — legacy-network family research.

These references remain independent projects with their own attribution and licensing. Inclusion in this bibliography is **not** a claim of endorsement or a claim that their rules were copied verbatim.

## Policy maintenance and audit trail

The shipped [`nanodns.ini`](../nanodns.ini) contains **124 patterns, zero active exceptions**, and four ordered non-filtering DNS addresses across two providers. The original profile was dated **10 October 2026**; Quad9 was used from **19 November 2026** until the **24 November 2026** migration.

Adding or removing a hostname requires its precise name, source, expected effect, reason for inclusion and false-positive analysis. Tests must be updated deliberately; do not silently increase the rule cap or weaken a blocking rule.

## Limits

A DNS name is not proof of malicious traffic. Shared CDN endpoints serve multiple parties, and broad patterns can cause collateral disruption. Runtime behavior remains governed by the installed resolver, network connectivity and firmware environment; see [threat model](THREAT_MODEL.md) and [coverage](COVERAGE.md).
