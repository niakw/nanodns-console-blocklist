# Couverture et preuves

**Langues :** [English (default)](COVERAGE.md) | Français

> Une liste DNS renforcée ne garantit pas l'isolement complet du réseau. Cette page distingue les règles présentes, les résultats observés et les validations manquantes.

## Périmètre

| Famille | Couverture | Preuve |
| --- | --- | --- |
| Services de la plateforme principale | Motifs de marque, domaines de services, alias historiques | Requêtes DNS correspondantes observées sur firmware 13.60 |
| Autres générations de consoles | Familles historiques de noms et de services | Tests statiques, pas de couverture matérielle exhaustive |
| Services d'éditeurs | Sélection de familles de noms | Tests statiques seulement |
| Réseaux de distribution partagés | Quelques alias exacts ; pas de blocage global du CDN | Risques de faux positifs connus |
| Sites de développement et de médias non ciblés | Aucun blocage volontaire | Tests statiques ; disponibilité réelle variable |

## Preuves disponibles

Le journal de test du **10 octobre 2026**, avec nanoDNS v0.4 et le profil **124 règles / 0 exception**, montre les écouteurs DNS locaux `127.0.0.1:53` et `[::1]:53`, les correspondances de noms protégés et des réponses locales `0.0.0.0` en A ou sans adresse en AAAA.

Il ne prouve ni que toutes les destinations sont connues, ni l'absence de trafic IP direct, ni la protection avant démarrage du payload. Le passage à Quad9 le 19 novembre 2026 puis à Control D/AdGuard le 24 novembre 2026 ne faisait pas partie de cette ancienne capture.

## Renforcement par rapport aux réglages d'origine

- **8 → 124** motifs de blocage livrés.
- **6 → 0** exceptions actives par défaut.
- **3 DNS de fournisseurs mélangés → Quad9 (historique) → 4 DNS sans filtrage ordonnés, deux fournisseurs :** Control D `76.76.2.0`, `76.76.10.0`, puis AdGuard DNS `94.140.14.140`, `94.140.14.141`.
- Tests automatiques de cohérence, absence de doublons, résolutions autorisées et configuration sécurisée.

Le [fork binaire optionnel](https://github.com/niakw/nanoDNS-13.60) ajoute la priorité de règles intégrées au code et d'autres contrôles. Le fichier INI ne possède pas ces fonctionnalités à lui seul.

Lancer `python3 -m unittest discover -s tests -v`, puis suivre l'[installation FR](INSTALL.fr.md). Pour une interdiction WAN intégrale, ajouter un pare-feu externe IPv4/IPv6.
