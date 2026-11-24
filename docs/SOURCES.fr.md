# Sources, crédits et provenance

**Langues :** [English (default)](SOURCES.md) | Français

Le dépôt fournit **une configuration originale et vérifiable**, sans redistribuer un exécutable tiers ni recopier intégralement un fichier hosts externe.

## Moteur d'origine

[Drakmor / nanoDNS](https://github.com/drakmor/nanoDNS) — auteur du payload, du format INI, du moteur de masques et de la résolution DNS UDP. La présente blocklist est indépendante et n'est pas une publication officielle de l'auteur.

## Résolution DNS sécurisée

[Control D](https://docs.controld.com/docs/free-dns) et [AdGuard DNS](https://adguard-dns.io/fr/public-dns.html) — adresses sans filtrage dans l'ordre : `76.76.2.0`, `76.76.10.0`, `94.140.14.140`, `94.140.14.141`. [Retrait de Quad9 en France](https://quad9.net/fr/news/blog/au-revoir-france/) le 24 novembre 2026 ; transport UDP non chiffré.

## Recherches communautaires complémentaires

Les noms historiques et les risques de faux positifs ont été rapprochés de recherches indépendantes :

- [Al-Azif / dns-config-watchdog](https://github.com/Al-Azif/dns-config-watchdog)
- [MagicStuffCL / liste DNS communautaire](https://github.com/MagicStuffCL/DnsblockListPS4PS5_Adguardhome)
- [cjrb007 / recherches DNS communautaires](https://github.com/cjrb007/ps5-dns-block)
- [Misl3d / liste communautaire](https://github.com/Misl3d/PS-dns-block)
- [ZixX3r / liste de services historiques](https://github.com/ZixX3r/Console-DNS-Block)

Chaque projet reste indépendant et conserve ses droits. La citation ne vaut ni affiliation ni copie intégrale de ses règles.

## Historique de la politique

Liste de **124 règles, sans exception active**, initialement datée du **10 octobre 2026**. Quad9 a été utilisé à partir du 19 novembre 2026 puis remplacé le **24 novembre 2026** par Control D et AdGuard. Pour proposer un changement, fournir le nom exact, la source, le comportement attendu et le risque de faux positif.

Consulter la [couverture](COVERAGE.fr.md), le [modèle de risque](THREAT_MODEL.fr.md) et l'[installation](INSTALL.fr.md).
