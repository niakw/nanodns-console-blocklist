<div align="center">

# nanoDNS Console Blocklist

### Filtre les requêtes indésirables sans sacrifier l'Internet utile.

**124 règles sélectives · 0 exception par défaut · Control D + AdGuard DNS**

**Langues :** [English (default)](README.md) · Français

[**Configuration**](nanodns.ini) · [**Notre nanoDNS PS5 13.60**](https://github.com/niakw/nanoDNS-Encore) · [**Guide français**](docs/INSTALL.fr.md) · [**Comparatif**](docs/COMPARISON.fr.md) · [**Limites**](docs/THREAT_MODEL.md)

</div>

---

## Une blocklist plus solide que la configuration d'origine

Les consoles modifiées, les émulateurs et les applications homebrew peuvent interroger des services de plateforme et d'éditeurs en arrière-plan. Il n'est pas nécessaire de couper tout Internet pour filtrer les noms connus.

**Cette blocklist renforce les réglages livrés avec [nanoDNS de Drakmor](https://github.com/drakmor/nanoDNS)** : **124 règles** au lieu de 8, **aucune exception par défaut** au lieu de 6, et **Control D sans filtrage, AdGuard sans filtrage en secours** pour les domaines non bloqués.

La liste reste publique, lisible, modifiable et testable hors ligne.

## Deux solutions : nanoDNS de Drakmor ou notre version PS5 13.60

Ce dépôt fournit **la blocklist `nanodns.ini` de 124 règles**, utilisable avec le [nanoDNS original de Drakmor](https://github.com/drakmor/nanoDNS).

Nous proposons également **[nanoDNS 13.60](https://github.com/niakw/nanoDNS-Encore)**, notre **payload complet alternatif et renforcé**, fondé sur le travail de Drakmor et adapté spécifiquement à la **PS5 sous firmware 13.60**. Contrairement au simple INI, cette version intègre les règles obligatoires dans l'ELF, les rend prioritaires sur les exceptions et améliore la sécurité ainsi que le cycle de vie du processus.

**Testé par un utilisateur sur PS5 13.60 :** la Release **0.4-13.60.2** démarre correctement, charge 124 règles sans exception, bloque les **5 requêtes DNS A observées** et a réussi un essai d'extinction/rallumage sans reproduction du problème initial (résultat d'arrêt rapporté par le testeur). **Les autres firmwares PS5 et la PS4 ne sont pas validés par tests utilisateurs.** La veille/reprise, les DNS autorisés vers l'amont, les requêtes AAAA et la stabilité prolongée restent à vérifier. Aucun des deux programmes ne remplace un pare-feu. Le nouveau profil DNS n'a pas été testé dans cet ancien essai.

**[Dépôt de notre nanoDNS PS5 13.60](https://github.com/niakw/nanoDNS-Encore)** · [Release actuelle](https://github.com/niakw/nanoDNS-Encore/releases/latest) · [ZIP ELF + INI dans la dernière Release](https://github.com/niakw/nanoDNS-Encore/releases/latest)

## Comparaison transparente

| Fonction | nanoDNS v0.4 original | **Notre blocklist** | Fork binaire optionnel |
| --- | --- | --- | --- |
| Règles par défaut | **8** | **124** | **124 obligatoires intégrées au code** |
| Exceptions actives | **6** | **0** | Les exceptions ne neutralisent pas les règles obligatoires |
| DNS amont | 3 résolveurs différents | **Control D + AdGuard sans filtrage** | Même ordre de 4 adresses |
| Couverture | Domaines de base | Plusieurs générations, éditeurs et alias connus | Idem + validation des réponses |
| Résolution des noms autorisés | Oui | **Préservée** | Préservée |
| Corrections de sécurité du processus | Originales | Non applicable au fichier INI | Arrêt et instances renforcés |
| Garantie de blocage de tout le réseau | **Non** | **Non** | **Non** |
| Extinction/rallumage testé sur firmware 13.60 | Non établi | Sans objet — fichier INI seul | **Essai utilisateur réussi sur PS5 13.60 avec 0.4-13.60.2** ; veille/reprise non validée |

La version d'origine accepte aussi des fichiers INI personnalisés. Les 8 règles et les 6 exceptions correspondent simplement à **son profil initial**. Notre INI seul ne rend pas les règles indésactivables : les protections de priorité et de vérification avancée appartiennent à [notre nanoDNS PS5 13.60](https://github.com/niakw/nanoDNS-Encore). [Comparatif détaillé](docs/COMPARISON.fr.md).

## Control D et AdGuard : deux fournisseurs, quatre IP

```ini
[upstream]
server=76.76.2.0
server=76.76.10.0
server=94.140.14.140
server=94.140.14.141
timeout_ms=1500
```

Le profil utilise Control D sans filtrage en priorité, AdGuard DNS sans filtrage en secours. Quad9 a cessé de servir les utilisateurs français le 24 novembre 2026 ([annonce](https://quad9.net/fr/news/blog/au-revoir-france/)). Les nouveaux profils n'ajoutent pas de filtrage antimalware ni publicitaire ; les 124 règles locales restent inchangées. Les deux DNS console restent **`127.0.0.1`**. Transport amont : UDP non chiffré. [Control D](https://docs.controld.com/docs/free-dns) · [AdGuard](https://adguard-dns.io/fr/public-dns.html).

## Installation sûre

Avant le premier démarrage, **bloque le WAN au niveau de la box/du pare-feu (IPv4 et IPv6)**, en conservant l'accès local au loader et au FTP. Sauvegarde `/data/nanodns/nanodns.ini`, remplace-le par [notre profil](nanodns.ini), démarre nanoDNS et vérifie la session en cours : **124 règles, 0 exception, écoute active et réponses bloquées**.

[**Guide complet français**](docs/INSTALL.fr.md) · [English installation](docs/INSTALL.md) · [Sécurité au démarrage](docs/SETUP_SAFETY.md)

## Des limites assumées

Le filtrage DNS n'est **pas un pare-feu**. Il ne protège pas contre les connexions directes aux adresses IP, les caches, les résolveurs alternatifs ou chiffrés, les communications avant démarrage ou les nouveaux domaines non connus. Les règles trop larges peuvent bloquer des services légitimes. Pour aucune fuite WAN, ajoute impérativement un filtrage réseau externe.

## Crédits

Code original : [Drakmor / nanoDNS](https://github.com/drakmor/nanoDNS). Recherche et maintenance de la liste : [niakw](https://github.com/niakw/nanodns-console-blocklist). Autres sources : [bibliographie](docs/SOURCES.md). Projet indépendant sous [GPL-3.0](LICENSE), sans affiliation avec les fabricants.

**Règles ouvertes. Limites explicites. Internet préservé.**
