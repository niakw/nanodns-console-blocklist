# Comparatif : nanoDNS d'origine, blocklist et fork renforcé

**Langues :** [English (default)](COMPARISON.md) | Français

Ce tableau compare les **réglages livrés par défaut**, pas les possibilités maximales du logiciel original.

| Fonction | nanoDNS 0.4 d'origine | Notre blocklist seule | Fork renforcé optionnel |
| --- | --- | --- | --- |
| Règles initiales de blocage | **8** | **124** | **124 règles obligatoires compilées** |
| Exceptions initiales | **6** | **0** | Impossible d'exempter un domaine déjà protégé |
| DNS amont | 3 fournisseurs distincts | **Quad9 sécurisé uniquement** | Quad9 sécurisé |
| Familles de domaines | Couverture initiale | Plusieurs générations, éditeurs et alias connus | Idem, avec priorité obligatoire |
| Résolution des noms autorisés | Oui | Via Quad9 | Via Quad9 |
| Modification par fichier INI | Oui | Oui | Oui, sauf règles obligatoires |
| Vérification des réponses DNS | Minimale | Dépend du binaire installé | Vérification question/réponse et alias protégés |
| Questions DNS multiples | Comportement original | Dépend du binaire | Rejet avant retransmission |
| Moteur de masques | Récursif | Dépend du binaire | Itératif et testé nativement |
| Chargements en doublon | Arrêt brutal de l'ancien processus | Dépend du binaire | Écoute exclusive, pas d'arrêt brutal |
| Historique des logs | Remplacé au démarrage | Dépend du binaire | Journal précédent conservé |
| Absence totale de fuite réseau | **Non garantie** | **Non garantie** | **Non garantie** |
| Extinction/réveil 13.60 validés | Non établi | Sans objet | **Validation matérielle attendue** |

## Pourquoi garder éventuellement le fork ?

Notre **fichier INI** renforce les règles par défaut, mais une autre configuration pourrait toujours les contourner. Le [fork binaire](https://github.com/niakw/nanoDNS-13.60) place les motifs obligatoires **dans le programme**, avant les exceptions, et améliore certains chemins d'arrêt et de vérification réseau. En revenant à nanoDNS original, ces protections supplémentaires disparaissent.

Le programme original sait charger des règles personnalisées. Les chiffres 8 et 6 désignent uniquement sa configuration officielle initiale.

## Limites et crédits

Ce projet n'est pas un pare-feu : IP directes, autres DNS, DNS chiffrés, trafic avant chargement et domaines non répertoriés restent hors périmètre. Une interdiction totale du WAN exige une protection externe.

Code original : [Drakmor](https://github.com/drakmor/nanoDNS). Configuration : [niakw](https://github.com/niakw/nanodns-console-blocklist). Voir [installation française](INSTALL.fr.md), [guide anglais](INSTALL.md), [sécurité](THREAT_MODEL.md) et [sources](SOURCES.md).
