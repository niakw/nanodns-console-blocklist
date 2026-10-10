# Setup safety and startup/reboot risks

**Policy mode: SELECTIVE.** This repository deliberately does not contain `*=0.0.0.0`; unrelated Internet hostnames are forwarded upstream when nanoDNS is running.

## Boot leak window

A **running DNS proxy is a prerequisite**, not a property of a saved file. Before nanoDNS runs, console code, a loader or a homebrew app may use another resolver, cached endpoints, direct IP connections or encrypted DNS. A previously downloaded update can even install without network access. The only practical way to suppress **all console WAN traffic during setup** is an **independent external network restriction**.

- **Cold boot without WAN** → local/offline loader → start nanoDNS → verify logs → set/confirm both DNS fields → verify actual overrides → optionally allow selective Internet at your own risk.
- **Full reboot** requires starting nanoDNS again; saved DNS `127.0.0.1` alone is not a complete firewall.
- **Rest-mode resume** requires checking the payload remains running; do not infer safety from a previous log.
- **Before using any public DNS-dependent loader**, acknowledge the bootstrap gap. A community DNS may implement different rules and is not covered by this project.
- **If zero unfiltered publisher access is mandatory:** leave WAN denied externally, including **IPv4 and IPv6**. A DNS-only approach cannot make that guarantee.

## What a successful check proves

- `config loaded: 2 upstream(s), 124 rule(s), 0 exception(s)` proves the active nanoDNS process loaded this policy.
- `listening on 127.0.0.1:53` proves a local DNS listener exists (at that instant).
- `query from=127.0.0.1` after the console DNS change shows an actual DNS query reached nanoDNS.
- `override matched` plus `data=0.0.0.0` for A (or no answers for AAAA) demonstrates the **specific lookup was blocked**.
- An unlisted domain such as `github.com` successfully forwarded upstream demonstrates **selective DNS forwarding for that query**.

**None** proves every PSN/publisher endpoint is known, that all IPv6/IP traffic is blocked, that updates cannot install, or that networking cannot bypass the resolver.

See **[complete install procedure (EN)](INSTALL.md)** and **[procédure sécurisée (FR)](INSTALL.fr.md)**.
