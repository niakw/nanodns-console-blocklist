# Contributing

Help extend coverage **without turning the policy into an accidental global Internet blocker**.

## Before opening a PR

- Prefer a specific, reproducible domain or narrow family of domains to wide, speculative matching.
- Include a public source or **redacted** nanoDNS log indicating the hostname and what service contacted it.
- Explain whether the change covers a console platform, game publisher, telemetry, update, login, CDN, or compatibility regression.
- Declare possible collateral blocking on third-party or shared infrastructure (Akamai, Cloudflare, Microsoft, etc.).
- Respect nanoDNS v0.4's **128-rule** ceiling; consolidate carefully and do not silently remove coverage.
- Keep `[exceptions]` empty unless a very explicit rationale and security review justify a change.

## Quality gate

```bash
python3 -m unittest discover -s tests -v
```

A contribution is not considered **hardware verified** merely because these tests pass. If tested on a console, specify the model, firmware, nanoDNS version, relevant log lines and what remained untested. Do not include account IDs, tokens, passwords, cookies, or unredacted device logs.

## Scope

The repository ships configuration and tests only. No copyrighted games, firmware images, exploit payloads, private keys, credentials or access-bypass guides belong here.
