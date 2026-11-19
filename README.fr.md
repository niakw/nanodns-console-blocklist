# nanoDNS Console Blocklist

**Langues :** [English (default)](README.md) · Français

**Liste sélective de 124 règles DNS, sans exception, destinée aux environnements PS4/PS5 homebrew et aux autres plateformes de jeu.**

Le profil [`nanodns.ini`](nanodns.ini) utilise le moteur libre [nanoDNS de Drakmor](https://github.com/drakmor/nanoDNS) pour répondre localement aux requêtes de domaines identifiés (PlayStation, Nintendo, Xbox, certains éditeurs), tout en transférant les autres noms à des résolveurs amont.

## DNS amont : Quad9 uniquement

```ini
[upstream]
server=9.9.9.9
server=149.112.112.112
timeout_ms=1500
```

Ces deux adresses sont celles du **service Quad9 sécurisé** (filtrage des domaines malveillants et validation DNSSEC), pas deux fournisseurs différents. **Aucun relais Cloudflare**. nanoDNS communique toujours avec les DNS amont en UDP non chiffré. Source : [Quad9](https://quad9.net/service/service-addresses-and-features/).

Les **DNS primaire et secondaire de la console** doivent tous deux pointer vers `127.0.0.1`, afin d'envoyer les questions au serveur local nanoDNS. Ne jamais inscrire Quad9 directement dans les champs DNS de la PS5 : cela contournerait les règles locales.

## Protection et limites

- **124 règles / zéro exception**. Les correspondances bloquées reçoivent `0.0.0.0` pour A, ou aucun enregistrement pour AAAA.
- Les noms autorisés continuent d'être résolus via Quad9.
- La liste est **sélective**, pas un blocage complet du réseau : noms inconnus, IP directes, DNS alternatifs/chiffrés, trafic antérieur au chargement du payload ou installation de packages déjà présents peuvent contourner cette protection.
- Pour empêcher **toute fuite WAN**, il faut aussi une restriction au niveau du routeur/pare-feu, IPv4 et IPv6.
- Les règles larges `*sony*`, `*playstation*` ou `*nintendo*` peuvent entraîner des faux positifs ; `a192.d.akamai.net` utilise une infrastructure CDN mutualisée.

## Installation et vérification

Avant le test, bloquer le WAN pour la console au niveau du réseau, puis sauvegarder le fichier existant `/data/nanodns/nanodns.ini`. Copier le nouveau [profil](nanodns.ini), redémarrer nanoDNS et vérifier dans les logs récents : `124 rule(s)`, `0 exception(s)`, écoute `127.0.0.1:53` et les deux upstreams Quad9. Tester une question interdite connue et une résolution autorisée sans essayer d'accéder à un serveur de mise à jour système.

Lire le [guide complet en français](docs/INSTALL.fr.md), la [procédure de sécurité](docs/SETUP_SAFETY.md), le [modèle de menaces](docs/THREAT_MODEL.md), les [sources](docs/SOURCES.md) et la [couverture](docs/COVERAGE.md).

## Crédits

**Payload original :** [Drakmor / nanoDNS](https://github.com/drakmor/nanoDNS). **Configuration et maintenance :** [niakw/nanodns-console-blocklist](https://github.com/niakw/nanodns-console-blocklist). Recherche communautaire complémentaire : voir [SOURCES.md](docs/SOURCES.md). Dépôt indépendant sous [GPL-3.0](LICENSE), sans affiliation avec Sony ou les autres fournisseurs de jeux.

**Statut :** tests statiques en CI ; aucune garantie de blocage total ni de sécurité du firmware par DNS seul.
