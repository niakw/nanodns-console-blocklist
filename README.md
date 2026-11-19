<div align="center">

# nanoDNS Console Blocklist

### Take control of console DNS — without cutting off the rest of the Internet.

**124 selective rules · 0 default exceptions · Quad9 Secure DNS**

[![DNS rules](https://img.shields.io/badge/Protected_patterns-124-394965)](nanodns.ini)
[![Default exceptions](https://img.shields.io/badge/Default_exceptions-0-28715e)](nanodns.ini)
[![Quad9](https://img.shields.io/badge/Resolver-Quad9-456b90)](https://docs.quad9.net/services/)
[![License](https://img.shields.io/badge/License-GPL--3.0-555)](LICENSE)

**English (default)** · [Français](README.fr.md)

[**Get the blocklist**](nanodns.ini) · [**Install in English**](docs/INSTALL.md) · [**Compare protections**](docs/COMPARISON.md) · [**Security model**](docs/THREAT_MODEL.md)

</div>

---

## More protection. Less unnecessary blocking.

Consoles running homebrew, emulators and media tools may resolve platform-service, telemetry and publisher domains in the background. Blocking *everything* makes daily use harder. Leaving every hostname unrestricted provides little control.

**nanoDNS Console Blocklist delivers a stronger, selective default policy for [nanoDNS by Drakmor](https://github.com/drakmor/nanoDNS).** It replaces the small original default ruleset with **124 reviewed DNS patterns**, removes the **six default bypass exceptions**, and routes unrelated DNS lookups through the **Quad9 secure resolver pair**.

The result is transparent, editable, auditable and practical: **block known unwanted hostnames while retaining DNS for permitted services.**

## How much stronger than the original?

| Capability | Original nanoDNS v0.4 defaults | **Console Blocklist** | Optional hardened runtime fork |
| --- | --- | --- | --- |
| Built-in/default deny patterns | **8** | **124** in the installable INI | **124 mandatory** masks compiled into the binary |
| Default bypass exceptions | **6** | **0** | Protected masks take priority over user exceptions |
| DNS upstreams | 3 mixed resolvers | **Quad9 Secure only** | Same Quad9 pair by default |
| Hostname coverage | Limited initial platform rules | Multiple generations, publisher endpoints and known aliases | Same policy with additional answer checks |
| Standard DNS on permitted sites | Available | **Preserved** | Preserved |
| Resolver code hardening | Original behavior | Not applicable — configuration only | Extra checks for replies, duplicate instances and shutdown |
| Guaranteed prevention of all outbound traffic | **No** | **No** | **No** |
| Hardware shutdown/wake validated here | Unverified | Not applicable | **Pending** |

**Important distinction:** the original nanoDNS can load a custom INI. Its eight rules and six exceptions are its **factory defaults**, not a limit. This repository ships a stronger **configuration**. Only the [separate hardened fork](https://github.com/niakw/nanoDNS-13.60) implements a mandatory embedded baseline and extra runtime security. [See full technical comparison](docs/COMPARISON.md).

## A clean, selective DNS path

```text
Console DNS (primary + secondary = 127.0.0.1)
                        |
                        v
              nanoDNS local resolver
                  /           \
      Denied hostname        Unlisted name
              |                    |
      Local 0.0.0.0 /            Quad9 Secure
      empty AAAA answer        9.9.9.9
                               149.112.112.112
```

Both upstream addresses belong to the **same Quad9 security-filtering service**. They are a primary and backup, not two providers. Quad9 filters known malicious domains and validates DNSSEC, but nanoDNS currently forwards through **ordinary, unencrypted UDP**. The **console DNS settings must both remain `127.0.0.1`**, never Quad9 directly. [Quad9 official documentation](https://docs.quad9.net/services/).

## Why this profile?

- **124 known deny patterns** across several console generations, publisher-service families and historical network aliases.
- **Zero default exceptions** — no intentional pass-through holes in the shipped list.
- **Selective rather than global blocking** — documentation, development tools and unrelated websites can still resolve.
- **No remote rules dependency** — a plain-text INI that can be inspected, versioned and tested offline.
- **Security-first deployment** — English installation documentation with a separate complete French guide.
- **Repeatable checks** — rule counts, duplicate detection, protected/allowed examples and Quad9-only settings verified by CI.

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
