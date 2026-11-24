# Coverage & evidence

**Language:** English (default) · [Français](COVERAGE.fr.md)

> A stronger **hostname blocklist** is not the same as complete network isolation. This project documents which patterns are included, what has been observed, and what remains untested.

## Scope by category

| Target family | Policy coverage | Evidence |
| --- | --- | --- |
| Primary console ecosystem | Broad brand-like masks, update/service names, historical aliases | Matching DNS lookups observed on firmware 13.60 |
| Additional console generations | Known legacy families, service names and update-related patterns | Offline tests; not exhaustively tested on hardware |
| Publisher and gaming services | Selected publisher hostname families | Offline tests; not exhaustively tested on hardware |
| Shared delivery infrastructure | Selected exact aliases, not a global CDN ban | Intentionally broad-risk; possible false positives |
| Ordinary development/media websites | Not deliberately blocked by the baseline | Static negative-control tests; runtime reachability depends on network |

## Real evidence (10 October 2026)

A console log from the original nanoDNS v0.4, using the **124-rule / 0-exception profile**, confirmed:

- The payload loaded all 124 rules and zero exception entries.
- It listened locally on IPv4 `127.0.0.1:53` and IPv6 `[::1]:53`.
- Observed target hostnames matched local override rules.
- For blocked A queries, the resolver replied with `0.0.0.0`. For matching AAAA queries, it returned no IPv6 answer.
- Repeated background queries were visible in that test session.

These observations do **not** demonstrate coverage of all possible endpoints, absence of direct-IP traffic, or successful blocking before payload startup. The Quad9 migration on 19 November 2026 and its replacement by Control D/AdGuard on 24 November 2026 were not part of the older console run.

## What is new relative to the original defaults?

- **8 → 124** shipped override patterns.
- **6 → 0** default bypass exceptions.
- **Three mixed upstreams → Quad9 (historical) → four ordered non-filtering upstreams across two providers:** Control D `76.76.2.0`, `76.76.10.0`, then AdGuard DNS `94.140.14.140`, `94.140.14.141`.
- Automated checks for policy count, duplicates, negative controls, DNS configuration, safe installation and documentation references.

The optional [runtime fork](https://github.com/niakw/nanoDNS-13.60) adds mandatory compiled rules and packet/lifecycle checks; those properties **are not delivered by the INI file itself**. See [comparison](COMPARISON.md).

## Validation

Run `python3 -m unittest discover -s tests -v` from the repository root. To confirm actual resolution on a console, use the [safe install checklist](INSTALL.md), confirm its DNS settings point to loopback, then inspect *fresh logs* for a blocked hostname taken directly from the INI and a permitted hostname.

Do not test by deliberately contacting operating-system update servers. For unknown endpoints or false positives, open a reproducible report with redacted logs and evidence. Broad masks and the exact shared-CDN entry can affect unrelated services.

**Limit:** DNS-only filtering cannot substitute for an external IPv4/IPv6 firewall when all unwanted WAN traffic must be denied.
