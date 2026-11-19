# Changelog

All notable updates to the policy and validation suite are recorded here.

## [Unreleased]

- **2026-11-19: Quad9-only upstreams.** Replaced Cloudflare (`1.1.1.1`) + Quad9 with Quad9's security-filtering primary (`9.9.9.9`) and backup (`149.112.112.112`), keeping the existing **124 overrides / 0 exceptions** intact.
- Updated English/French install guides, source attribution, tests and expected startup logs. This is a configuration change; **no new hardware validation is claimed**.

- Replaced abbreviated installation guidance with a safety-first **LAN-only / WAN-denied** workflow and stage-by-stage verification.
- Added full **English and French** instructions: backup the exact INI, launch/restart loader and payload, read startup logs, set both console DNS fields to loopback, inspect actual blocked queries, and cautiously re-enable selective Internet only when residual risk is acceptable.
- Documented cold boot, rest mode, loader bootstrap gaps, DNS-vs-IP fail-closed behavior, upstream testing, log rotation, rollback and troubleshooting.
- Added documentation contract tests to CI; at that stage there were **no DNS rule or upstream changes** (the Quad9-only change is documented above).

- Community beta documentation, reproducible static checks and contribution/security guidance.
- Roadmap: evaluate longer-duration logs, check unlisted console/publisher traffic and false positives before a versioned stable release.

## [0.1.0] — 2026-10-10

- Initial **selective** `nanodns.ini` publication: **124 override rules / 0 exceptions**.
- Covers PlayStation, Nintendo, Xbox, and selected game-publisher families; retains upstream DNS for all unlisted names.
- Includes exact `a192.d.akamai.net` alias (known shared-CDN collateral-risk).
- PS5 nanoDNS v0.4 field log confirms policy load and override responses for *observed* PlayStation hostnames; broader compatibility remains unverified.

> `0.1.0` denotes an initial repository baseline, **not** a GitHub Release or a claim of complete platform coverage.
