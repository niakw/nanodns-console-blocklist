# Original nanoDNS vs Console Blocklist vs hardened fork

**Language:** English (default) | [Français](COMPARISON.fr.md)

This compares **default shipped configurations**, not the maximum capabilities of the original program.

| Feature | nanoDNS 0.4 stock | Our standalone blocklist | Optional hardened fork |
| --- | --- | --- | --- |
| Default deny rules | **8** | **124** | **124 compiled mandatory masks** |
| Default bypass exceptions | **6** | **0** | Protected names bypass all custom exceptions |
| Default upstreams | 3 different providers | **Quad9 Secure pair only** | Quad9 Secure pair only |
| Hostname families | Core platform defaults | Multiple generations, publishers and historical aliases | Same list, enforced in code |
| Allowed DNS | Forwarded | Forwarded through Quad9 | Forwarded through Quad9 |
| User-editable file | Yes | Yes | Yes, without weakening compiled protected rules |
| DNS upstream reply validation | Basic transaction checking | Depends on installed payload | Question / answer / protected alias checks |
| Unusual multiple-question DNS | Original runtime behavior | Depends on installed payload | Rejected before forwarding |
| Wildcard matching | Recursive | Depends on installed payload | Iterative, with native regression tests |
| Duplicate launches | Kills previous process | Depends on installed payload | No forced kill; exclusive UDP listener |
| Log lifecycle | Current log replaced | Depends on installed payload | Previous log retained and size capped |
| No network leaks of any kind | **Not guaranteed** | **Not guaranteed** | **Not guaranteed** |
| Firmware 13.60 shutdown/power-on trial | Not established here | Not applicable | **User-tested successfully on PS5 13.60, runtime 0.4-13.60.2**; rest/resume untested |

## Runtime alternatives

Use the **[original nanoDNS by Drakmor](https://github.com/drakmor/nanoDNS)** with this project's `nanodns.ini` when you only want to customize its DNS configuration. Alternatively, our independent **[nanoDNS 13.60 runtime](https://github.com/niakw/nanoDNS-13.60)** provides a complete ELF with the same 124-rule default policy plus compiled mandatory masks and runtime hardening. **Its 0.4-13.60.2 release passed a user startup, blocked A-query and normal shutdown/power-on trial on PS5 firmware 13.60.** No hardware validation is claimed for other PS5 firmware or PS4.

[Download our 13.60 Release](https://github.com/niakw/nanoDNS-13.60/releases/tag/v0.4-13.60.2) · [Ready-to-copy ZIP](https://github.com/niakw/nanoDNS-13.60/releases/download/v0.4-13.60.2/nanodns-13.60-v0.4-13.60.2-install.zip). The ZIP installs an ELF as well as the INI; do not run it alongside the original payload.

## Key distinction

The **124 rules and zero exceptions** in the independent configuration strengthen default hostname coverage. They remain **editable** and can be bypassed by a different user configuration. The optional [hardened runtime](https://github.com/niakw/nanoDNS-13.60) also **compiles mandatory rules**, prioritizes them over exceptions, and adds packet validation and process-lifecycle changes. Reverting to stock nanoDNS loses those runtime protections, even with the same INI.

The original software can load custom blocklists; eight rules and six exceptions describe only its **unmodified defaults**.

## Non-guarantees and provenance

The blocklist does not act as a firewall or guarantee that every unwanted service is known. It does not handle direct IP connections, alternate or encrypted DNS, TCP DNS or network access before payload startup. For strict isolation, configure an external router/firewall deny policy on both IP families.

Original source: [Drakmor / nanoDNS](https://github.com/drakmor/nanoDNS). Policy: [niakw / Console Blocklist](https://github.com/niakw/nanodns-console-blocklist). See [source bibliography](SOURCES.md), [coverage](COVERAGE.md), [security model](THREAT_MODEL.md) and [English installation](INSTALL.md).
