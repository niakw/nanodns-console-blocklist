# Threat model and limits

**Language:** English (default) · [Français](THREAT_MODEL.fr.md)

nanoDNS Console Blocklist is a **selective policy for a local UDP DNS proxy**. Its objective is to reduce DNS lookups to known platform-service and publisher hostnames while leaving unrelated DNS available.

## In scope

- Detect matches against **124 configured hostname patterns**.
- Answer blocked A queries locally with `0.0.0.0` and blocked AAAA requests without IPv6 addresses, using the installed nanoDNS behavior.
- Ship **zero default bypass exceptions** and direct permitted names to the four ordered non-filtering Control D/AdGuard upstream addresses.
- Provide reproducible static tests and evidence-based maintenance.

## Out of scope

- Direct connections to IPv4/IPv6 addresses, cached addresses or previously downloaded packages.
- Alternative resolvers, encrypted DNS, app-specific network stacks or DNS over TCP.
- Traffic before jailbreak/payload startup, during failed boot, or while nanoDNS is not active.
- Hostnames absent from the list, new service infrastructure and opaque CDN aliases.
- Firmware or game-update guarantees, anonymity, account protection or full firewall enforcement.

## Startup safety

**Before installation and after each cold boot**, keep the console behind an **external WAN-deny rule** if leakage is unacceptable. Deploy `/data/nanodns/nanodns.ini`, start the resolver, make both console DNS settings `127.0.0.1` and verify intercepted requests in the **current** log. A saved file and a loopback DNS value do not prove the payload is running.

If nanoDNS is absent, ordinary loopback DNS may fail, but **direct-IP access and alternate DNS may still succeed**. Only an independent router/firewall can enforce WAN isolation before startup, including IPv6.

## Resolver and false positives

The four upstreams are Control D `76.76.2.0`, `76.76.10.0`, followed by AdGuard DNS `94.140.14.140`, `94.140.14.141`. Both profiles are unfiltered; unlike the prior Quad9 profile they provide no additional malware/ad filtering. The payload uses plaintext UDP.

The list includes deliberately **broad vendor-name patterns** and at least one **exact name on shared CDN infrastructure**. A matching DNS hostname can be legitimate; investigate false positives with redacted logs and the narrowest supported change.

## Config versus hardened runtime

The standalone policy file **does not force compiled mandatory rules**, sanitize arbitrary upstream answers, or fix process shutdown. Those enhancements are specific to the optional [hardened runtime fork](https://github.com/niakw/nanoDNS-13.60) and still require physical-console validation. See [technical comparison](COMPARISON.md).

Read [English installation](INSTALL.md), [French installation](INSTALL.fr.md) and [startup safety](SETUP_SAFETY.md) before allowing WAN access.
