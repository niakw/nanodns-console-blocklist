# Changelog

**Language:** English (default) · [Français](CHANGELOG.fr.md)

## 2026-11-24 — DNS provider migration

- Quad9 withdrawal from France: replace both upstreams with Control D (unfiltered) first, AdGuard DNS (non-filtering) as fallback, in order `76.76.2.0`, `76.76.10.0`, `94.140.14.140`, `94.140.14.141`.
- Preserve all 124 block patterns, zero exceptions, loopback DNS and timeout. No additional malware filtering is claimed.

## Unreleased — 2026-11-19

- **Quad9-only upstreams:** use `9.9.9.9` and `149.112.112.112` for the same secure, threat-blocking service. No secondary external provider.
- Keep the **124 deny rules** and **zero default exceptions** unchanged.
- Rebuild marketing-focused English and French README files, with accurate original-versus-blocklist-versus-hardened-fork comparisons.
- Add explicit links to the correct-language installation manuals, source acknowledgements, security boundaries and published evidence.
- Document safe startup, independent router/firewall requirements, and the distinction between config-only and binary-enforced safeguards.
- Add policy and documentation regression checks.
- Make the separately maintained [nanoDNS 13.60](https://github.com/niakw/nanoDNS-Encore) a prominent alternative to Drakmor's original runtime in English/French README and comparisons; document the version-specific PS5 firmware 13.60 user test and links to the Release/ZIP without claiming validation on other firmware.

## 0.1.0 — 2026-10-10

- Initial selective blocklist with **124 DNS overrides and zero exceptions**.
- Coverage expanded beyond the original resolver's **eight default patterns** across several console generations, selected publisher families and historical aliases.
- Console logs confirmed interception of observed DNS lookups; **not** complete coverage of all network traffic.
- Supplied static tests and source attribution.

> A changelog entry, CI success or source-only test is not proof of hardware shutdown safety, complete network isolation or operating-system update prevention.
