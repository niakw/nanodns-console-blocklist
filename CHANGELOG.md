# Changelog

All notable updates to the policy and validation suite are recorded here.

## [Unreleased]

- Community beta documentation, reproducible static checks and contribution/security guidance.
- Roadmap: evaluate longer-duration logs, check unlisted console/publisher traffic and false positives before a versioned stable release.

## [0.1.0] — 2026-10-10

- Initial **selective** `nanodns.ini` publication: **124 override rules / 0 exceptions**.
- Covers PlayStation, Nintendo, Xbox, and selected game-publisher families; retains upstream DNS for all unlisted names.
- Includes exact `a192.d.akamai.net` alias (known shared-CDN collateral-risk).
- PS5 nanoDNS v0.4 field log confirms policy load and override responses for *observed* PlayStation hostnames; broader compatibility remains unverified.

> `0.1.0` denotes an initial repository baseline, **not** a GitHub Release or a claim of complete platform coverage.
