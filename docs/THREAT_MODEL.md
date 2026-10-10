# Threat model: what this does—and does not—protect

This file is a **selective DNS denylist** for the independent nanoDNS payload.

## In scope

- Intercept **DNS lookups handled by a running nanoDNS instance**.
- Return `0.0.0.0` for matching A requests; for matching AAAA requests nanoDNS v0.4 returns a successful response with **no IPv6 answer**.
- Reduce selected accidental DNS-based contact to PlayStation, Nintendo, Xbox and game-publisher names.
- Resolve unlisted domains through the configured upstream resolvers, enabling **selective** Internet access.

## Explicitly out of scope

- **No promise** that PS4/PS5 firmware updates or game updates are impossible.
- Connections made **before nanoDNS starts**, on a different DNS resolver, with cached addresses, through DNS-over-HTTPS/TLS/TCP or directly to an IPv4/IPv6 address.
- Firewalling, TLS interception, packet inspection, emulator/game anti-cheat bypass, anonymity or guaranteed console account safety.
- Detection of every future endpoint or opaque CDN hostname.
- All network traffic of emulator guest systems; behavior depends on each emulator's networking implementation.

## Preventing leaks during installation and restart

**First use:** isolate the console from WAN through a router/firewall or WAN-disconnected router (IPv4 and IPv6), but retain a LAN path if you need FTP or a locally usable payload loader. Install `/data/nanodns/nanodns.ini`, launch or restart nanoDNS, inspect the initial log, set **both** console DNS fields to `127.0.0.1`, and inspect **subsequent** DNS queries for `override matched` plus a blocked response.

**Cold boot / crash:** a file on disk or console DNS pointed at loopback does not mean the payload is running. Restart it, inspect a current log, then decide whether to allow WAN. A loader that requires a public DNS host may create a separate unfiltered bootstrap interval; do not call that safe.

**DNS fail-closed vs Internet fail-closed:** when a console points to loopback but nanoDNS is stopped, *ordinary name resolution* usually fails. That does **not** make IP forwarding fail-closed. Direct IPv4/IPv6 IP traffic, another resolver, DNS-over-HTTPS or cached connections can still reach destinations if WAN is available.

See the full [English installation walkthrough](INSTALL.md), [French installation walkthrough](INSTALL.fr.md) and [startup safety checklist](SETUP_SAFETY.md).

## Why not block everything?

A global `*=0.0.0.0` policy would prevent legitimate DNS resolution (artwork, GitHub, tools, updates of unrelated software). This project **deliberately does not include** such a rule. Instead, its known target names are blocked, with the accepted trade-off that unknown hosts may still resolve.

## Why a firewall is different

A network firewall can enforce destination IP/port policies outside the console and even when nanoDNS has not yet started. High-assurance firmware preservation should combine restrictive network access policy, disabled automatic updates and careful control of installed packages/media. DNS-only protection cannot offer the same guarantee.

## False positives

- `*sony*`, `*playstation*`, `*nintendo*` match **any** hostname containing those character sequences, including unrelated domains.
- `a192.d.akamai.net` is an **exact** name, but historically associated with Sony while using a **shared** CDN operator.
- Entire game publisher domains are blocked, including websites, sign-in and updates that some users may want.

No diagnostic log or user test data is committed by default. Public reports should omit tokens, usernames, cookies and identifiable network metadata.
