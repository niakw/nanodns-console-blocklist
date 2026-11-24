<div align="center">

# nanoDNS Console Blocklist

### Take control of console DNS — without cutting off the rest of the Internet.

**124 selective rules · 0 default exceptions · Control D + AdGuard DNS**

[![DNS rules](https://img.shields.io/badge/Protected_patterns-124-394965)](nanodns.ini)
[![Default exceptions](https://img.shields.io/badge/Default_exceptions-0-28715e)](nanodns.ini)
[![Resolvers](https://img.shields.io/badge/DNS-Control_D%20%2B%20AdGuard-456b90)](https://docs.controld.com/docs/free-dns)
[![License](https://img.shields.io/badge/License-GPL--3.0-555)](LICENSE)

**English (default)** · [Français](README.fr.md)

[**Get the blocklist**](nanodns.ini) · [**Our nanoDNS for PS5 13.60**](https://github.com/niakw/nanoDNS-Encore) · [**Install in English**](docs/INSTALL.md) · [**Compare protections**](docs/COMPARISON.md) · [**Security model**](docs/THREAT_MODEL.md)

</div>

---

## More protection. Less unnecessary blocking.

Consoles running homebrew, emulators and media tools may resolve platform-service, telemetry and publisher domains in the background. Blocking *everything* makes daily use harder. Leaving every hostname unrestricted provides little control.

**nanoDNS Console Blocklist delivers a stronger, selective default policy for [nanoDNS by Drakmor](https://github.com/drakmor/nanoDNS).** It replaces the small original default ruleset with **124 reviewed DNS patterns**, removes the **six default bypass exceptions**, and routes unrelated DNS lookups through the **Control D unfiltered resolvers, with AdGuard non-filtering fallback**.

The result is transparent, editable, auditable and practical: **block known unwanted hostnames while retaining DNS for permitted services.**

## Choose your nanoDNS: Drakmor original or our PS5 13.60 edition

This repository supplies the **124-rule `nanodns.ini` blocklist**, which you can use with [Drakmor's original nanoDNS](https://github.com/drakmor/nanoDNS).

For a **complete alternative payload**, we also maintain **[nanoDNS 13.60](https://github.com/niakw/nanoDNS-Encore)**, an independent hardened runtime based on Drakmor's work, specifically prepared for **PS5 firmware 13.60**. Unlike an INI-only replacement, it embeds the protected rules in the binary, enforces them before user exceptions, and includes security and process-lifecycle improvements.

**PS5 firmware 13.60 — real-user tested:** release **0.4-13.60.2** successfully started, loaded 124 rules with 0 exceptions, blocked all **5 observed A DNS queries**, and completed a normal shutdown/power-on trial without recurrence of the previously reported problem (power-cycle result user-reported). **Other PS5 firmwares and PS4 have not been user-validated.** Rest/resume, permitted upstream lookups, AAAA and long-duration stability still require tests. Neither version replaces a firewall. The new resolver profile is not part of the historical hardware test.

**[Explore our nanoDNS 13.60 repository](https://github.com/niakw/nanoDNS-Encore)** · [Latest Release](https://github.com/niakw/nanoDNS-Encore/releases/latest) · [ELF + INI ZIP on latest release](https://github.com/niakw/nanoDNS-Encore/releases/latest)

## How much stronger than the original?

| Capability | Original nanoDNS v0.4 defaults | **Console Blocklist** | Optional hardened runtime fork |
| --- | --- | --- | --- |
| Built-in/default deny patterns | **8** | **124** in the installable INI | **124 mandatory** masks compiled into the binary |
| Default bypass exceptions | **6** | **0** | Protected masks take priority over user exceptions |
| DNS upstreams | 3 mixed resolvers | **Control D + AdGuard, unfiltered** | Same ordered four addresses by default |
| Hostname coverage | Limited initial platform rules | Multiple generations, publisher endpoints and known aliases | Same policy with additional answer checks |
| Standard DNS on permitted sites | Available | **Preserved** | Preserved |
| Resolver code hardening | Original behavior | Not applicable — configuration only | Extra checks for replies, duplicate instances and shutdown |
| Guaranteed prevention of all outbound traffic | **No** | **No** | **No** |
| Firmware 13.60 shutdown/power-on user test | Not established | Not applicable — INI only | **Passed on PS5 13.60 with runtime 0.4-13.60.2**; rest/resume unverified |

**Important distinction:** the original nanoDNS can load a custom INI. Its eight rules and six exceptions are its **factory defaults**, not a limit. This repository ships a stronger **configuration**. Only our [PS5 13.60 hardened nanoDNS runtime](https://github.com/niakw/nanoDNS-Encore) implements a mandatory embedded baseline and extra runtime security. [See full technical comparison](docs/COMPARISON.md).

## A clean, selective DNS path

```text
Console DNS (primary + secondary = 127.0.0.1)
                        |
                        v
              nanoDNS local resolver
                  /           \
      Denied hostname        Unlisted name
              |                    |
      Local 0.0.0.0 /            Control D
      empty AAAA answer        76.76.2.0 / 76.76.10.0
                               AdGuard fallback
                               94.140.14.140 / 94.140.14.141
```

The ordered upstream profile uses Control D (unfiltered) first, AdGuard DNS (non-filtering) as fallback: `76.76.2.0`, `76.76.10.0`, `94.140.14.140`, `94.140.14.141`. Quad9 stopped serving French users on 24 November 2026 ([announcement](https://quad9.net/news/blog/au-revoir-france/)). Neither new profile adds malware or ad filtering; the 124 local rules remain unchanged. Upstream transport is **ordinary, unencrypted UDP**. Both console DNS settings remain **`127.0.0.1`**. [Control D](https://docs.controld.com/docs/free-dns) · [AdGuard](https://adguard-dns.io/en/public-dns.html).

## Why this profile?

- **124 known deny patterns** across several console generations, publisher-service families and historical network aliases.
- **Zero default exceptions** — no intentional pass-through holes in the shipped list.
- **Selective rather than global blocking** — documentation, development tools and unrelated websites can still resolve.
- **No remote rules dependency** — a plain-text INI that can be inspected, versioned and tested offline.
- **Security-first deployment** — English installation documentation with a separate complete French guide.
- **Repeatable checks** — rule counts, duplicate detection, protected/allowed examples and ordered four-address settings verified by CI.

## Install without a blind spot

**Before exposing a firmware-sensitive console to Internet access, block outbound WAN at your router/firewall (IPv4 + IPv6).** Preserve a local/offline loader. Back up `/data/nanodns/nanodns.ini`; copy our [`nanodns.ini`](nanodns.ini) to that exact path; start nanoDNS, then set *both console DNS fields* to `127.0.0.1`. Verify **fresh current-session logs** show `124 rule(s)`, `0 exception(s)`, a live listener and blocked answers.

**[Complete English installation guide](docs/INSTALL.md)** · [Guide complet en français](docs/INSTALL.fr.md) · [Startup/reboot safety](docs/SETUP_SAFETY.md)

## What this does **not** guarantee

DNS filtering is **not a firewall**. It cannot reliably stop direct-IP connections, cached addresses, other DNS resolvers, encrypted DNS, TCP DNS, connections made before the payload starts or newly discovered domains. Broad pattern matches can also affect innocent hostnames, and shared CDN names deserve special care. **For zero unwanted WAN traffic, keep an independent router/firewall policy.**

Evidence for tested DNS lookups is documented separately from claims requiring real hardware or network verification. See [coverage](docs/COVERAGE.md), [threat model](docs/THREAT_MODEL.md) and [comparison](docs/COMPARISON.md).

## Documentation and credits

[Install (EN)](docs/INSTALL.md) · [Install (FR)](docs/INSTALL.fr.md) · [Comparison (EN)](docs/COMPARISON.md) · [Comparatif (FR)](docs/COMPARISON.fr.md) · [Sources](docs/SOURCES.md) · [Contributing](CONTRIBUTING.md) · [Changelog](CHANGELOG.md)

**Original payload:** [Drakmor / nanoDNS](https://github.com/drakmor/nanoDNS). **Blocklist research and maintenance:** [niakw](https://github.com/niakw/nanodns-console-blocklist). Additional independent research is credited in [SOURCES.md](docs/SOURCES.md). GPL-3.0, independent community project, no affiliation with commercial device manufacturers.

---

**Open rules. Clear limits. Useful Internet.**
