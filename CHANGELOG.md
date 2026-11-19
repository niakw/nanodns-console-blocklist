# Changelog

**Language:** English (default) · [Français](CHANGELOG.fr.md)

## Unreleased — 2026-11-19

- **Quad9-only upstreams:** use `9.9.9.9` and `149.112.112.112` for the same secure, threat-blocking service. No secondary external provider.
- Keep the **124 deny rules** and **zero default exceptions** unchanged.
- Rebuild marketing-focused English and French README files, with accurate original-versus-blocklist-versus-hardened-fork comparisons.
- Add explicit links to the correct-language installation manuals, source acknowledgements, security boundaries and published evidence.
- Document safe startup, independent router/firewall requirements, and the distinction between config-only and binary-enforced safeguards.
- Add policy and documentation regression checks.

## 0.1.0 — 2026-10-10

- Initial selective blocklist with **124 DNS overrides and zero exceptions**.
- Coverage expanded beyond the original resolver's **eight default patterns** across several console generations, selected publisher families and historical aliases.
- Console logs confirmed interception of observed DNS lookups; **not** complete coverage of all network traffic.
- Supplied static tests and source attribution.

> A changelog entry, CI success or source-only test is not proof of hardware shutdown safety, complete network isolation or operating-system update prevention.
