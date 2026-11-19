# Sources, crédits et provenance

**Langues :** [English (default)](SOURCES.md) | Français

Le dépôt fournit **une configuration originale et vérifiable**, sans redistribuer un exécutable tiers ni recopier intégralement un fichier hosts externe.

## Moteur d'origine

[Drakmor / nanoDNS](https://github.com/drakmor/nanoDNS) — auteur du payload, du format INI, du moteur de masques et de la résolution DNS UDP. La présente blocklist est indépendante et n'est pas une publication officielle de l'auteur.

## Résolution DNS sécurisée

[Quad9 — adresses officielles](https://docs.quad9.net/fr/services/) — `9.9.9.9` et `149.112.112.112` correspondent au même service avec filtrage des menaces et validation DNSSEC. Le payload utilise toujours de l'UDP non chiffré vers ces résolveurs.

## Recherches communautaires complémentaires

Les noms historiques et les risques de faux positifs ont été rapprochés de recherches indépendantes :

- [Al-Azif / dns-config-watchdog](https://github.com/Al-Azif/dns-config-watchdog)
- [MagicStuffCL / liste DNS communautaire](https://github.com/MagicStuffCL/DnsblockListPS4PS5_Adguardhome)
- [cjrb007 / recherches DNS communautaires](https://github.com/cjrb007/ps5-dns-block)
- [Misl3d / liste communautaire](https://github.com/Misl3d/PS-dns-block)
- [ZixX3r / liste de services historiques](https://github.com/ZixX3r/Console-DNS-Block)

Chaque projet reste indépendant et conserve ses droits. La citation ne vaut ni affiliation ni copie intégrale de ses règles.

## Historique de la politique

Liste de **124 règles, sans exception active**, initialement datée du **10 octobre 2026**. Les résolveurs Quad9 ont été configurés le **19 novembre 2026**. Pour proposer un changement, fournir le nom exact, la source, le comportement attendu et le risque de faux positif.

Consulter la [couverture](COVERAGE.fr.md), le [modèle de risque](THREAT_MODEL.fr.md) et l'[installation](INSTALL.fr.md).
