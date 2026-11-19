# Contribuer

**Langues :** [English (default)](CONTRIBUTING.md) | Français

Les contributions doivent renforcer la **couverture, la fiabilité ou la clarté**, sans ajouter de contournements non justifiés.

## Proposer un domaine

Fournir le nom exact ou le motif le plus restreint possible, la source, la raison du blocage, son effet attendu et le risque de faux positif. Ne pas publier de captures de trafic contenant des données personnelles.

## Qualité de la politique

- Préférer des hôtes précis aux masques trop larges.
- Évaluer les CDN partagés avant tout blocage.
- Conserver un format INI réellement compatible avec nanoDNS.
- Conserver **zéro exception active par défaut**, sauf examen explicite.
- Respecter la limite actuelle de **128 règles** du moteur.
- Garder les deux DNS sécurisés Quad9, sauf changement documenté.

## Tests

Lancer `python3 -m unittest discover -s tests -v`, mettre à jour les tests si la politique change et contrôler la documentation d'installation en anglais et en français.

Voir [les limites](docs/THREAT_MODEL.fr.md), [les sources](docs/SOURCES.fr.md) et [le projet original](https://github.com/drakmor/nanoDNS). Projet communautaire indépendant sous [GPL-3.0](LICENSE).
