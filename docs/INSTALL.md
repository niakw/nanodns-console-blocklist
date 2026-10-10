# Safe installation — PS4 / PS5 (nanoDNS v0.4)

**Goal:** install the selective 124-rule profile while **minimizing unfiltered network exposure**. This is an operational checklist, not a claim that DNS filtering stops every network connection. Read the [threat model](THREAT_MODEL.md) before connecting an Internet-facing console.

> [!CAUTION]
> **Never assume the PS4/PS5 is protected just because the `nanodns.ini` file exists. nanoDNS must be running, console DNS must point to it, and the relevant DNS queries must be observed matching an override.**
>
> For the **first boot, firmware-sensitive consoles should remain isolated from the public Internet** until the sequence below has been checked. The only way to exclude *all* pre-payload/direct-IP traffic is a separately enforced network restriction (router/firewall/WAN isolation). This blocklist alone cannot promise zero leaks.

## 0 — Decide your risk level *before* starting

| Your priority | Recommended network posture |
| --- | --- |
| **No outbound Internet before payload/filter validation** | Keep PS4/PS5 on an isolated LAN with **WAN denied externally** while you prepare, load nanoDNS and validate it. |
| **Internet for selected homebrew/emulator services after validation** | Use this selective policy and re-enable WAN **only after** the checks below; understand the remaining DNS bypass and direct-IP risks. |
| **Absolutely no external connection to console/publisher infrastructure** | DNS-only cannot certify that property. Keep an independent firewall / WAN restriction in place; prefer local-only tools. |

An isolated LAN means LAN communication can still work (e.g. FTP from a Mac), but **all console Internet egress is denied** by a router/firewall rule that covers **both IPv4 and IPv6**, or by physically disconnecting the WAN from a router while preserving its LAN. Merely changing the console's DNS server or blocking TCP/UDP port 53 is **not** equivalent to blocking outbound traffic.

**Do not rely on a public community DNS** during initial setup. If your exploit/loader cannot start offline or via a trusted local route, there may be an unavoidable unfiltered interval when using that method; **stop and reassess rather than treating that interval as safe**. This repository does not supply an offline loader or exploit.

## 1 — Offline preflight (WAN still denied)

- [ ] Confirm you can start your homebrew loader **without depending on PSN or an unfiltered public DNS**. Record the path before restarting.
- [ ] Disable the PS4/PS5's **automatic system-software downloads/installations** and **automatic game/app updates** in available settings. Menu names depend on console/firmware.
- [ ] Disable Internet-connected rest-mode behaviors if you do not need them.
- [ ] Check for **previously downloaded/pending update packages**; a DNS filter does not remove or prevent installation of an already-downloaded update. Do **not** trigger an update check as a test.
- [ ] Ensure local transfer/FTP access works *inside the isolated LAN*. If not, use an offline storage method where supported.
- [ ] Download the policy on a trusted computer and inspect the plain-text file before copying it.

**Checkpoint A:** console WAN denied; no automatic update action pending; local loader/transfer route understood.

## 2 — Install or edit the exact INI

1. On the console, **back up** the current `/data/nanodns/nanodns.ini` outside the active configuration filename (for example, `nanodns.ini.bak`).
2. Copy the repository's [**`nanodns.ini`**](../nanodns.ini) as **exactly** `/data/nanodns/nanodns.ini`. Do not upload it as `nanodns_v3.ini`, `nanodns.ini.txt` or another filename and expect automatic loading.
3. Verify the file is a **plain-text INI**, not an AdGuard/hosts list; it must have `[general]`, `[upstream]`, `[overrides]`, `[exceptions]`. No `0.0.0.0 domain.name` hosts-format lines and no `||domain^` AdGuard syntax.
4. Check these values in the installed INI:

   ```ini
   [general]
   bind=127.0.0.1
   bind6=::1

   [upstream]
   server=1.1.1.1
   server=9.9.9.9
   timeout_ms=1500

   [overrides]
   # 124 selective rules; never replace with *=0.0.0.0

   [exceptions]
   # empty
   ```

5. Leave the **124-rule** baseline and zero exceptions as provided. nanoDNS v0.4 supports **at most 128 rules**, so adding a large hosts file directly will not work. This configuration **does not block all Internet**.

The two public DNS servers above belong **inside nanoDNS only**. They resolve **unmatched** names; they must **not** be added as a public DNS bypass in the console's network settings.

**Checkpoint B:** path, format, bind, rule count, exceptions and backup checked; console WAN still denied.

## 3 — Start / restart the loader and nanoDNS *while still isolated*

1. Launch your **already available local/offline loader** and start the nanoDNS payload. If nanoDNS was already running, **restart the nanoDNS payload** so it reads the new INI.
2. **A whole-console reboot is not normally required just to load new rules.** Reboot only if your particular homebrew loader requires it. Any whole-console reboot stops in-memory payloads; nanoDNS must be launched again.
3. Keep the console **WAN blocked during and after** this step; do not reconnect Internet merely because the homebrew menu is open.
4. Read the **first lines** of `/data/nanodns/nanodns.log`. nanoDNS **overwrites this log at each startup**: save any diagnostic copy *before* relaunching if needed.

### First log gate — must pass

```text
NanoDNS v0.4
[nanodns] bind IPv4: 127.0.0.1:53
[nanodns] bind IPv6: [::1]:53
[nanodns] config loaded: 2 upstream(s), 124 rule(s), 0 exception(s), timeout=1500ms
[nanodns] upstream[0] = 1.1.1.1
[nanodns] upstream[1] = 9.9.9.9
[nanodns] listening on 127.0.0.1:53
[nanodns] listening on [::1]:53
```

Ordering and extra messages can vary. `listening on 127.0.0.1:53` and **124 rule(s), 0 exception(s)** are decisive indicators of correct startup configuration, **not yet proof that the console is using nanoDNS**.

If the INI did not load, any listener is missing, the version is incompatible, or the rule count differs: **keep WAN denied and fix before proceeding**. If IPv6 bind fails, investigate rather than assuming IPv6 traffic is secured.

**Checkpoint C:** running payload, correct file and listeners evidenced in the log.

## 4 — Configure BOTH console DNS fields (still isolated)

On PS5, go to **Settings → Network → Settings → Set Up Internet Connection → select connection → Advanced Settings → DNS Settings: Manual**. The exact menus on PS4 or different system languages may differ.

| Console network setting | Value |
| --- | --- |
| IP address | Automatic / existing LAN configuration |
| DHCP host name | Do not specify / existing setting |
| **Primary DNS** | **`127.0.0.1`** |
| **Secondary DNS** | **`127.0.0.1`** |
| MTU | Automatic / existing setting |
| Proxy | Do not use / existing setting |

**Never enter `1.1.1.1`, `9.9.9.9`, `8.8.8.8` or a public/community DNS as the console's secondary resolver.** This may bypass your local rules. The console fields use an IPv4 loopback address; `bind6=::1` makes nanoDNS listen on IPv6 loopback but **does not establish that every possible IPv6 or alternative-resolver path is controlled**.

Save the settings. If the console reports a failed PlayStation Network / Internet connection test, **do not 'fix' it by switching to automatic or public DNS**. Tests that contact PSN can fail **precisely because the rules blocked PSN**.

**Checkpoint D:** both displayed DNS settings read `127.0.0.1`; WAN still denied.

## 5 — Confirm actual DNS interception, not just startup

Keep the WAN gate closed. Examine `/data/nanodns/nanodns.log` **after** changing the PS4/PS5 network settings. If the console makes a normal background request for a blocked Sony name, you should see entries resembling:

```text
[nanodns] query from=127.0.0.1:... qname=ps5.np.playstation.net qtype=A(1) ...
[nanodns] override matched *playstation* -> 0.0.0.0 for ps5.np.playstation.net
[nanodns] response via=override ... qtype=A(1) ... answers=1
[nanodns]   answer[0] ... data=0.0.0.0
[nanodns] response via=override-nodata ... qtype=AAAA(28) ... answers=0
```

The A and AAAA entries may occur separately. **A response code of `NOERROR` does not mean the Sony service was allowed**: for blocked A records the data is `0.0.0.0`; for blocked AAAA records the answer set is empty.

- [ ] **Observed at least one `query from=127.0.0.1` after DNS change**.
- [ ] **Observed at least one `override matched` for a known blocked domain**, or verified the resolver using a deliberately issued DNS query from an *on-console* tool if available.
- [ ] Matched A gives **`0.0.0.0`**; matched AAAA gives **zero IPv6 answers**.
- [ ] No sign that the INI silently fell back to default rules or that the payload terminated.

**If no DNS requests appear, the log cannot confirm filtering.** It may mean that no DNS request has occurred, that caches are being used, that traffic is bypassing nanoDNS or that the network settings did not take effect. **Do not remove the external WAN restriction on that basis.**

**Avoid testing via “check for system update”, PSN sign-in, Store login or a live firmware download.** Passive log inspection and safe, locally generated queries are preferred.

### Testing from a Mac? Important

`dig @127.0.0.1 ...` **on your Mac queries the Mac**, not the PS5. Conversely `dig @<PS5-LAN-IP> ...` normally fails with this configuration because nanoDNS is deliberately listening on **loopback only** (`bind=127.0.0.1`). Do **not** change to `bind=0.0.0.0` merely for testing without understanding the LAN exposure.

**Checkpoint E:** console-side interception observed and response behavior checked. This remains DNS-only evidence.

## 6 — Optional controlled WAN return (selective Internet only)

Only if you **accept the limitations** in [THREAT_MODEL.md](THREAT_MODEL.md) and need online homebrew/emulator resources:

1. Keep nanoDNS **running**, verify console DNS remains `127.0.0.1` in **both fields**, and inspect the current session log once more.
2. **Remove the temporary router/WAN restriction** only when you accept that **unlisted hosts, direct IP addresses, encrypted/alternate DNS and pre-existing connections can reach the Internet**. Retain the restriction if avoiding *any* possible publisher contact is mandatory.
3. Launch a **known permitted** homebrew function that legitimately requests an unlisted name (for example, public project metadata on `github.com`). Confirm the function actually succeeds.
4. Check the current nanoDNS log for a matching DNS query and an upstream response from **`1.1.1.1` or `9.9.9.9`**. Upstream log wording varies. **No upstream query observed means this test is inconclusive**, even if an application loaded cached content.
5. Continue to observe the console log for blocked names and unexpected traffic; report missing endpoints with **redacted** evidence.

If the access you need fails, **do not 'fix' it by setting automatic DNS or a public secondary server**. Restore WAN isolation before diagnosis.

**Checkpoint F (selective mode):** known targeted DNS is blocked **and** known permitted traffic is observed via upstream; residual bypass risks remain.

## 7 — After every reboot, crash, rest mode or loader restart

- The nanoDNS payload is a **process**, not a firmware-level permanent DNS filter. **A full reboot means it must be started again**, unless you have a separately verified auto-start arrangement. Auto-start claims must be tested after a cold boot.
- With console DNS kept at `127.0.0.1`, ordinary DNS normally **fails closed for name resolution** while nanoDNS is absent. **This does not stop direct-IP traffic, existing addresses or alternative resolvers.**
- **Safest routine:** keep external WAN denied before/during boot → launch the local loader → launch nanoDNS → inspect startup logs → verify both DNS fields and block responses → optionally restore selective WAN when the remaining risk is acceptable.
- **Rest-mode/resume is not equivalent to a validated cold boot.** Check that nanoDNS is still listening and that new queries are logged.
- To change rules in the future: copy/modify `nanodns.ini` → reload/restart nanoDNS → inspect startup **again** → test both blocked and permitted resolution. Do not assume file edits apply immediately.
- If your loader cannot start without external DNS after a reboot, plan a **local/offline bootstrap** before enabling Internet. A public exploit DNS is not equivalent to verified filtering.

## 8 — Recovery / failure scenarios

| Symptom | Action while WAN remains denied |
| --- | --- |
| No nanoDNS process after boot | Launch it using the offline/local loader; check log startup, then resume. |
| No DNS resolution | Confirm `bind=127.0.0.1`, both console DNS fields, process/listener and file path. |
| First log says fewer than **124** rules | Restore this repository's exact `nanodns.ini`, restart payload; max is **128** rules. |
| No `query from=` after DNS change | Recheck console network settings; inspect whether an application really generated a DNS lookup. |
| Sony hostname resolves publicly | Keep WAN blocked; verify the DNS path is actually loopback and the hostname matches a rule. |
| Internet connection test shows failure | Sony connectivity tests may call intentionally blocked Sony endpoints; use an unrelated allowed service instead. |
| Site / emulator metadata breaks | Inspect the queried hostname. Broad brand masks or `a192.d.akamai.net` may cause collateral blocking. |
| No Internet after reboot | Expected while nanoDNS is not running and both DNS fields point at loopback. Start it first. |
| Cannot use a public DNS-dependent loader while isolated | **Do not assume a leak-free setup is possible**. Prefer a local bootstrapping route or enforce an external firewall. |
| Want to revert | While WAN isolated, restore the backup INI and restart nanoDNS; only change console DNS to other values if you deliberately accept the resulting exposure. |

## 9 — Periodic checks and evidence handling

- nanoDNS v0.4 **overwrites its log on every start**. Collect a diagnostic copy **before restarting** to preserve evidence.
- It can log frequent retries to a blocked name, including many AAAA queries; repetition alone does not mean the filter failed.
- This policy intentionally blocks **publisher authentication, service and update domains**, so PlayStation Store/PSN and many legitimate online game features are expected to fail.
- Publisher-owned hostnames may change; an absence of unblocked domains in one log is **not** proof of exhaustive coverage.
- Redact IPs, usernames, account names, tokens and local device identifiers before sharing logs publicly.
- Disable automatic update/download settings independently; keep a backup of the tested configuration.
- For users who cannot accept any bypass, **do not restore WAN based on DNS logs alone**.

**Final check: blocked names intercepted; permitted names work as intended; known bypass limitations accepted. Only then consider the console ready for selective online use.**

See [coverage and measured evidence](COVERAGE.md) and [upstream nanoDNS](https://github.com/drakmor/nanoDNS).
