# Modèle de risque et limites

**Langues :** [English (default)](THREAT_MODEL.md) | Français

nanoDNS Console Blocklist est une **politique DNS sélective** pour un résolveur local UDP, et non un pare-feu.

## Ce qui est couvert

- **124 motifs de noms de domaine** connus sont bloqués par le payload lorsqu'il reçoit les requêtes.
- Pour un nom bloqué, A retourne `0.0.0.0`, AAAA ne renvoie pas d'adresse, selon le comportement du moteur installé.
- Le fichier livré ne contient **aucune exception active**.
- Les noms autorisés sont transmis au service sécurisé **Quad9**.

## Ce qui n'est pas couvert

Les IP directes, caches DNS, résolveurs alternatifs ou chiffrés, DNS sur TCP, piles réseau propres aux applications, noms inconnus et trafic avant démarrage du payload. Le filtrage ne garantit donc ni une absence totale de connexion Internet, ni la prévention des mises à jour système.

## Installation et redémarrage

En cas d'exigence stricte, **bloquer le WAN depuis le routeur/pare-feu**, en IPv4 et IPv6, avant le démarrage. Copier le fichier `/data/nanodns/nanodns.ini`, démarrer nanoDNS, renseigner les deux DNS de la console avec `127.0.0.1` et vérifier des requêtes bloquées dans **le journal actuel**.

Sans nanoDNS, une résolution classique vers le loopback peut échouer, mais des connexions IP directes ou un autre DNS peuvent toujours fonctionner. Seule une restriction externe couvre la période précédant le payload.

## Quad9 et faux positifs

`9.9.9.9` et `149.112.112.112` sont deux adresses du **même service Quad9 sécurisé**. La validation DNSSEC par Quad9 n'implique pas que le transfert UDP du payload soit chiffré.

Les motifs larges et un alias exact d'un CDN partagé peuvent toucher des noms légitimes. Documenter les faux positifs et éviter les exceptions générales.

## Différence avec le fork

Un fichier INI ne rend pas les règles obligatoires et ne peut pas modifier le code de nettoyage des processus ou de validation des réponses. Seul le [fork renforcé optionnel](https://github.com/niakw/nanoDNS-13.60) ajoute ces mécanismes, sous réserve de validation matérielle. Voir le [comparatif](COMPARISON.fr.md) et le [guide d'installation](INSTALL.fr.md).
