# Sécurité et signalements

**Langues :** [English (default)](SECURITY.md) | Français

Ce dépôt publie une liste DNS communautaire, **pas un pare-feu**. La protection s'applique uniquement aux requêtes reçues par nanoDNS lorsque celui-ci est actif. Les accès directs par IP, DNS alternatifs, DNS chiffrés, caches, connexions avant démarrage et domaines inconnus restent hors périmètre.

Pour une interdiction stricte de toute sortie Internet, configurer un pare-feu ou une règle de blocage WAN au niveau du routeur, **IPv4 et IPv6**.

Signaler les défauts avec le firmware, la version du payload, le profil utilisé, un nom de domaine reproductible, le résultat observé et les journaux anonymisés. Éviter toute publication de données personnelles, de jetons ou d'adresses privées.

Le projet utilise [nanoDNS de Drakmor](https://github.com/drakmor/nanoDNS) et [Quad9](https://docs.quad9.net/fr/services/) comme résolveur configuré ; il est indépendant de l'auteur du payload et de tout fabricant de console.

Consulter [le modèle de risque](docs/THREAT_MODEL.fr.md), [la couverture](docs/COVERAGE.fr.md) et [l'installation](docs/INSTALL.fr.md).
