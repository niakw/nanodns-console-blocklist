# Install & operate

This repository contains a **nanoDNS configuration file**, not a DNS server or a PS4/PS5 jailbreak.

## Prerequisites

- A PS4 or PS5 where the independent [Drakmor nanoDNS](https://github.com/drakmor/nanoDNS) payload can already run. Hardware observations to date are limited to nanoDNS v0.4 on **PS5 firmware 13.60**.
- A way to copy a plain-text file to the console (for example, a file manager or FTP).
- A backup of the original `/data/nanodns/nanodns.ini`.

## Steps

1. Copy this repository's [`nanodns.ini`](../nanodns.ini) to **`/data/nanodns/nanodns.ini`**, replacing your previous config only after backing it up.
2. Start or **restart** nanoDNS (rules load on startup).
3. In console network advanced DNS settings, choose **manual** and set:
   - **Primary DNS:** `127.0.0.1`
   - **Secondary DNS:** `127.0.0.1`
4. Keep `[general] bind=127.0.0.1` in the INI. nanoDNS v0.4 also listens at `[::1]:53` for IPv6 DNS *queries* via `bind6=::1`.
5. Review `/data/nanodns/nanodns.log` (logging is enabled even with `debug=0`).

Do **not** enter `1.1.1.1` or `9.9.9.9` as the PS5's DNS secondary. Those are upstream resolvers **inside** nanoDNS for *unmatched* names only.

## Expected log evidence

```text
[nanodns] config loaded: 2 upstream(s), 124 rule(s), 0 exception(s), timeout=1500ms
[nanodns] listening on 127.0.0.1:53
[nanodns] listening on [::1]:53
[nanodns] override matched *playstation* -> 0.0.0.0 for ps5.np.playstation.net
[nanodns] response via=override ... qtype=A(1) ... answers=1
[nanodns] response via=override-nodata ... qtype=AAAA(28) ... answers=0
```

These example lines reflect an observed nanoDNS v0.4 PS5 log; they do not mean all network requests have been filtered.

For a **known unblocked** domain such as `github.com`, expect upstream forwarding. Verify it using an application that actually requests that domain. Avoid testing a firmware update itself.

## Troubleshooting / rollback

| Symptom | Check |
| --- | --- |
| No DNS / no Internet | Is nanoDNS currently running? Does `bind` match both DNS settings? |
| No `override matched` | Confirm requested hostname, console DNS settings, INI path and payload restart. |
| File reports fewer than 124 rules | Check for invalid lines or the 128-rule ceiling; use repository version verbatim. |
| Wanted site is blocked | Inspect broad brand masks and `a192.d.akamai.net`; file an issue with a reproducible DNS name. |
| “Internet test” fails | Sony's own connectivity test may use blocked PlayStation endpoints even if unrelated sites resolve. |
| Need network access before payload starts | DNS interception does not run before payload startup; plan this separately. |

To revert, stop nanoDNS, restore the previously backed-up config, and restart the payload. Restore the console network DNS settings only when you understand the resulting exposure. If the payload is not running while the console points to `127.0.0.1`, domain resolution typically fails rather than falling back to the public DNS upstream.

## Important limits

nanoDNS v0.4 implements UDP DNS listening/forwarding. This configuration does **not** block traffic addressed directly to known IPs, DNS-over-HTTPS resolvers, DNS-over-TCP, already-cached addresses, connections established before the payload starts or any application bypassing the configured resolver. For high-assurance isolation, use an independently enforced network firewall policy and disable automatic software downloads separately.
