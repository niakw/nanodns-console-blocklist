# Contributing

**Language:** English (default) · [Français](CONTRIBUTING.fr.md)

Contributions are welcome when they improve **correctness, coverage or clarity** without weakening the DNS policy.

## Propose a hostname

Provide the exact hostname or the narrowest possible wildcard, the source where it was observed, the type of service, expected effect, and potential false positives. Do not submit full traffic captures with personal network identifiers.

## Rule quality

- Prefer exact names or narrow suffix families over excessively broad matches.
- Check whether a candidate alias uses **shared CDN infrastructure** and could disrupt unrelated services.
- Keep the source INI valid for nanoDNS (not hosts-file or another blocklist syntax).
- Preserve **zero active default exceptions**. Proposed exceptions require an explicit risk review.
- Stay within the resolver's **128-rule limit**, or coordinate an implementation change with the runtime project.
- Preserve both Quad9 secure upstream addresses unless there is a documented migration.

## Validation

Run `python3 -m unittest discover -s tests -v`. Update the test baseline and coverage evidence if rules change. Confirm allowed-domain negative controls remain meaningful, and check the installation guides in English and French before merging.

See [threat model](docs/THREAT_MODEL.md), [sources](docs/SOURCES.md) and [original runtime](https://github.com/drakmor/nanoDNS). This project is independent, community-maintained and GPL-3.0 licensed.
