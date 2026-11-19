<div align="center">

# nanoDNS Console Blocklist

### Filtre les requêtes indésirables sans sacrifier l'Internet utile.

**124 règles sélectives · 0 exception par défaut · Quad9 sécurisé**

**Langues :** [English (default)](README.md) · Français

[**Configuration**](nanodns.ini) · [**Guide français**](docs/INSTALL.fr.md) · [**Comparatif**](docs/COMPARISON.fr.md) · [**Limites**](docs/THREAT_MODEL.md)

</div>

---

## Une blocklist plus solide que la configuration d'origine

Les consoles modifiées, les émulateurs et les applications homebrew peuvent interroger des services de plateforme et d'éditeurs en arrière-plan. Il n'est pas nécessaire de couper tout Internet pour filtrer les noms connus.

**Cette blocklist renforce les réglages livrés avec [nanoDNS de Drakmor](https://github.com/drakmor/nanoDNS)** : **124 règles** au lieu de 8, **aucune exception par défaut** au lieu de 6, et **Quad9 sécurisé uniquement** pour les domaines non bloqués.

La liste reste publique, lisible, modifiable et testable hors ligne.

## Comparaison transparente

| Fonction | nanoDNS v0.4 original | **Notre blocklist** | Fork binaire optionnel |
| --- | --- | --- | --- |
| Règles par défaut | **8** | **124** | **124 obligatoires intégrées au code** |
| Exceptions actives | **6** | **0** | Les exceptions ne neutralisent pas les règles obligatoires |
| DNS amont | 3 résolveurs différents | **Quad9 uniquement** | Quad9 uniquement |
| Couverture | Domaines de base | Plusieurs générations, éditeurs et alias connus | Idem + validation des réponses |
| Résolution des noms autorisés | Oui | **Préservée** | Préservée |
| Corrections de sécurité du processus | Originales | Non applicable au fichier INI | Arrêt et instances renforcés |
| Garantie de blocage de tout le réseau | **Non** | **Non** | **Non** |
| Extinction/réveil matériel prouvés | Non | Sans objet | **À valider** |

La version d'origine accepte aussi des fichiers INI personnalisés. Les 8 règles et les 6 exceptions correspondent simplement à **son profil initial**. Notre INI seul ne rend pas les règles indésactivables : les protections de priorité et de vérification avancée appartiennent au [fork optionnel](https://github.com/niakw/nanoDNS-13.60). [Comparatif détaillé](docs/COMPARISON.fr.md).

## Quad9 : un seul fournisseur, deux IP

```ini
[upstream]
server=9.9.9.9
server=149.112.112.112
timeout_ms=1500
```

Ces adresses utilisent toutes deux le **service Quad9 sécurisé**. Les DNS primaire **et** secondaire configurés dans la console doivent en revanche rester `127.0.0.1` pour que les requêtes passent par nanoDNS. Le protocole amont utilisé par nanoDNS demeure **UDP non chiffré**. [Documentation Quad9](https://docs.quad9.net/fr/services/).

## Installation sûre

Avant le premier démarrage, **bloque le WAN au niveau de la box/du pare-feu (IPv4 et IPv6)**, en conservant l'accès local au loader et au FTP. Sauvegarde `/data/nanodns/nanodns.ini`, remplace-le par [notre profil](nanodns.ini), démarre nanoDNS et vérifie la session en cours : **124 règles, 0 exception, écoute active et réponses bloquées**.

[**Guide complet français**](docs/INSTALL.fr.md) · [English installation](docs/INSTALL.md) · [Sécurité au démarrage](docs/SETUP_SAFETY.md)

## Des limites assumées

Le filtrage DNS n'est **pas un pare-feu**. Il ne protège pas contre les connexions directes aux adresses IP, les caches, les résolveurs alternatifs ou chiffrés, les communications avant démarrage ou les nouveaux domaines non connus. Les règles trop larges peuvent bloquer des services légitimes. Pour aucune fuite WAN, ajoute impérativement un filtrage réseau externe.

## Crédits

Code original : [Drakmor / nanoDNS](https://github.com/drakmor/nanoDNS). Recherche et maintenance de la liste : [niakw](https://github.com/niakw/nanodns-console-blocklist). Autres sources : [bibliographie](docs/SOURCES.md). Projet indépendant sous [GPL-3.0](LICENSE), sans affiliation avec les fabricants.

**Règles ouvertes. Limites explicites. Internet préservé.**
