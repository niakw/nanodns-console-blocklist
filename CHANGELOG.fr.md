# Historique des versions

**Langues :** [English (default)](CHANGELOG.md) | Français

## 24 novembre 2026 — Migration DNS

- Retrait de Quad9 en France : Control D sans filtrage en priorité, AdGuard DNS sans filtrage en secours, dans l'ordre `76.76.2.0`, `76.76.10.0`, `94.140.14.140`, `94.140.14.141`.
- Conserver les 124 motifs, zéro exception, les écoutes locales et le délai. Aucun filtrage antimalware supplémentaire revendiqué.

## En cours — 19 novembre 2026

- **Quad9 uniquement** : `9.9.9.9` et `149.112.112.112`, deux adresses du même service de filtrage des menaces.
- Conservation des **124 règles** de blocage et de **zéro exception par défaut**.
- Refonte marketing des README anglais et français et ajout d'un comparatif explicite avec nanoDNS d'origine et le fork binaire optionnel.
- Corrections des liens d'installation selon la langue, crédits des sources et description des limites réelles.
- Documentation d'installation hors WAN, de reprise, de vérification des logs et des conditions de retrait du fork.
- Contrôles CI des règles et des documents.
- Présentation visible de [notre nanoDNS 13.60](https://github.com/niakw/nanoDNS-Encore) comme alternative au payload original de Drakmor, avec lien Release/ZIP et périmètre des tests utilisateurs PS5 firmware 13.60, sans validation des autres firmwares.

## 0.1.0 — 10 octobre 2026

- Première version de la liste sélective : **124 règles DNS / aucune exception**.
- Extension de la configuration initiale de nanoDNS (8 motifs / 6 exceptions), avec familles de services et alias historiques supplémentaires.
- Journaux de console confirmant le blocage des seules requêtes DNS observées ; absence de preuve d'une isolation réseau complète.

**Important :** une CI verte ne prouve pas la stabilité de l'extinction ni le blocage de tout trafic Internet.
