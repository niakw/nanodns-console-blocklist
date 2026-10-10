# Changelog

All notable updates to the policy and validation suite are recorded here.

## [Unreleased]

- Replaced abbreviated installation guidance with a safety-first **LAN-only / WAN-denied** workflow and stage-by-stage verification.
- Added full **English and French** instructions: backup the exact INI, launch/restart loader and payload, read startup logs, set both console DNS fields to loopback, inspect actual blocked queries, and cautiously re-enable selective Internet only when residual risk is acceptable.
- Documented cold boot, rest mode, loader bootstrap gaps, DNS-vs-IP fail-closed behavior, upstream testing, log rotation, rollback and troubleshooting.
- Added documentation contract tests to CI; **no DNS rule or upstream changes**.

- Community beta documentation, reproducible static checks and contribution/security guidance.
- Roadmap: evaluate longer-duration logs, check unlisted console/publisher traffic and false positives before a versioned stable release.

## [0.1.0] — 2026-10-10

- Initial **selective** `nanodns.ini` publication: **124 override rules / 0 exceptions**.
- Covers PlayStation, Nintendo, Xbox, and selected game-publisher families; retains upstream DNS for all unlisted names.
- Includes exact `a192.d.akamai.net` alias (known shared-CDN collateral-risk).
- PS5 nanoDNS v0.4 field log confirms policy load and override responses for *observed* PlayStation hostnames; broader compatibility remains unverified.

> `0.1.0` denotes an initial repository baseline, **not** a GitHub Release or a claim of complete platform coverage.
