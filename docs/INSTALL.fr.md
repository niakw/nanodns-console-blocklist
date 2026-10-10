# Installation sécurisée — PS4 / PS5 (nanoDNS v0.4)

**Objectif :** installer les **124 règles sélectives** sans exposer inutilement la console aux serveurs Sony, Nintendo, Xbox ou aux éditeurs pendant la configuration. Ce guide réduit les risques de fuite DNS, mais **un DNS n'est pas un pare-feu**. Voir [les limites de sécurité](THREAT_MODEL.md).

> [!CAUTION]
> **Avoir un fichier `nanodns.ini` sur le disque ne suffit pas.** Le payload doit fonctionner, les deux DNS de la console doivent pointer vers `127.0.0.1`, puis les journaux doivent montrer de véritables requêtes interceptées.
>
> **Pour le premier démarrage, garder l'accès Internet WAN bloqué par un équipement externe** jusqu'à la vérification du payload. nanoDNS seul ne garantit pas l'absence totale de fuite, notamment avant son lancement ou pour les connexions directes par IP.

## 0 — Isoler la console AVANT de commencer

Choisir la situation adaptée :

| Besoin | Mesure |
| --- | --- |
| Préparer sans aucune connexion Internet PS4/PS5 | Réseau **local uniquement** avec accès WAN bloqué sur la box / le pare-feu pour la console, **IPv4 et IPv6**. |
| Garder Internet partiellement utilisable ensuite | Retirer temporairement le blocage WAN **après** tous les contrôles, en acceptant les risques résiduels DNS/IP. |
| Empêcher absolument tout contact extérieur | Garder une **restriction réseau indépendante**. Une blocklist DNS seule ne le garantit pas. |

Une isolation **LAN sans WAN** permet de continuer à utiliser un ordinateur et le FTP sur le réseau local. On peut aussi déconnecter la liaison WAN du routeur tout en conservant son LAN. Un simple changement de DNS, ou un blocage du port 53, ne bloque **pas** tout le trafic IP sortant.

**Attention au loader :** si ton point d'entrée jailbreak exige un site ou un DNS public pour démarrer, il peut exister une phase non filtrée. N'appelle pas cette phase « sécurisée ». Prépare plutôt un lanceur utilisable localement/hors ligne ou une restriction au niveau du routeur avant de poursuivre.

## 1 — Préparation hors ligne

- [ ] Bloquer le WAN de la console **avant** de l'allumer / de modifier la configuration.
- [ ] Confirmer que le loader est accessible **en local et sans PSN**.
- [ ] Désactiver les **téléchargements et installations automatiques** du logiciel système et des jeux/applications dans les paramètres disponibles.
- [ ] Désactiver la connexion Internet en mode repos si elle n'est pas nécessaire.
- [ ] Vérifier les **mises à jour déjà téléchargées ou en attente** : un DNS ne les supprime pas et n'empêche pas leur installation locale.
- [ ] Vérifier que l'accès FTP ou le gestionnaire de fichiers fonctionne sur le LAN isolé.
- [ ] Télécharger et lire le [fichier officiel du dépôt](../nanodns.ini) depuis un ordinateur.

**Contrôle A :** WAN toujours bloqué, mise à jour automatique désactivée et méthode de chargement local connue.

## 2 — Modifier `nanodns.ini`, sauvegarder, transférer

1. Faire une **sauvegarde** du fichier actuel `/data/nanodns/nanodns.ini` (ex. `nanodns.ini.bak`).
2. Transférer [**`nanodns.ini`**](../nanodns.ini) à l'emplacement **exact** `/data/nanodns/nanodns.ini`.
3. Vérifier le nom : pas de `nanodns_v3.ini`, pas de `nanodns.ini.txt`. Le format est **INI**, pas une liste hosts ou AdGuard.
4. Contrôler au minimum :

   ```ini
   [general]
   bind=127.0.0.1
   bind6=::1

   [upstream]
   server=1.1.1.1
   server=9.9.9.9
   timeout_ms=1500

   [overrides]
   # 124 règles sélectives ; aucune règle globale *=0.0.0.0

   [exceptions]
   # Aucune exception
   ```

5. Conserver les **124 règles / 0 exception** ; nanoDNS v0.4 limite la configuration à **128 règles**.

Les DNS publics `1.1.1.1` et `9.9.9.9` sont **uniquement les upstreams de nanoDNS** pour les domaines non bloqués. **Ils ne doivent pas être indiqués dans les deux champs DNS de la PS5.**

**Contrôle B :** bon chemin, bon fichier, sauvegarde conservée ; WAN toujours bloqué.

## 3 — Redémarrer le loader / nanoDNS (toujours SANS WAN)

1. Ouvrir le loader local/offline déjà installé sur la console.
2. Lancer **nanoDNS** ; s'il tournait déjà, **redémarrer le payload** pour recharger le fichier.
3. Un **redémarrage complet de la console n'est normalement pas nécessaire** pour recharger le fichier. Si le loader l'exige, redémarrer la console **WAN coupé**, relancer le loader, puis relancer nanoDNS.
4. Ouvrir les **premières lignes** du journal `/data/nanodns/nanodns.log`. Il est **écrasé à chaque lancement** de nanoDNS : sauvegarder l'ancien journal avant le redémarrage si nécessaire.

### Premiers logs attendus

```text
NanoDNS v0.4
[nanodns] bind IPv4: 127.0.0.1:53
[nanodns] bind IPv6: [::1]:53
[nanodns] config loaded: 2 upstream(s), 124 rule(s), 0 exception(s), timeout=1500ms
[nanodns] upstream[0] = 1.1.1.1
[nanodns] upstream[1] = 9.9.9.9
[nanodns] listening on 127.0.0.1:53
[nanodns] listening on [::1]:53
```

Ces lignes confirment que le processus a **chargé sa configuration et écoute le DNS**. **Elles ne prouvent pas encore que la PS5 utilise ce DNS !**

En cas d'absence du listener, de mauvais nombre de règles ou d'erreur de chargement, **ne pas rétablir Internet**.

**Contrôle C :** nanoDNS actif, configuration 124/0 et listener local actif.

## 4 — Modifier les DEUX champs DNS de la console (WAN toujours bloqué)

**PS5 :** Paramètres → Réseau → Paramètres → Configurer la connexion Internet → sélectionner la connexion → Paramètres avancés → Paramètres DNS : Manuel. Les libellés PS4 et certaines langues diffèrent.

| Champ | Valeur |
| --- | --- |
| Adresse IP | Automatique ou configuration LAN existante |
| Nom d'hôte DHCP | Ne pas spécifier |
| **DNS principal** | **`127.0.0.1`** |
| **DNS secondaire** | **`127.0.0.1`** |
| MTU | Automatique |
| Proxy | Ne pas utiliser |

**Jamais de DNS secondaire public** (`8.8.8.8`, `1.1.1.1`, `9.9.9.9`, DNS communautaire) dans la console : cela pourrait contourner nanoDNS.

Dans le fichier, `bind6=::1` active l'écoute DNS en IPv6 local ; cela **ne garantit pas** que toute communication IPv6 ou tout autre résolveur sera intercepté.

Un échec du test de connexion PlayStation Network peut être **normal** puisque PSN est volontairement bloqué. **Ne pas remettre les DNS en automatique pour contourner ce test.**

**Contrôle D :** les deux DNS affichés sont `127.0.0.1` ; WAN toujours bloqué.

## 5 — Revérifier les logs APRÈS modification des DNS

Lire **à nouveau** `/data/nanodns/nanodns.log` et chercher des événements récents. Exemple réel du profil :

```text
[nanodns] query from=127.0.0.1:... qname=ps5.np.playstation.net qtype=A(1) ...
[nanodns] override matched *playstation* -> 0.0.0.0 for ps5.np.playstation.net
[nanodns] response via=override ... qtype=A(1) ... answers=1
[nanodns]   answer[0] ... data=0.0.0.0
[nanodns] response via=override-nodata ... qtype=AAAA(28) ... answers=0
```

Checklist :

- [ ] `query from=127.0.0.1` : la console ou un programme a interrogé nanoDNS **depuis le changement DNS**.
- [ ] `override matched` : un domaine visé a bien été intercepté.
- [ ] Pour `A` : résultat **`0.0.0.0`**.
- [ ] Pour `AAAA` : **0 réponse** IPv6. `NOERROR` seul ne signifie pas que le domaine a été autorisé.
- [ ] Aucun rechargement en configuration par défaut ni arrêt du payload.

**Aucune requête dans les logs ?** On ne peut pas confirmer la protection. Cela peut venir d'un cache, d'aucune activité réseau, d'un contournement DNS ou d'un mauvais réglage. **Garder le WAN bloqué** en attendant le diagnostic.

Ne surtout **pas** déclencher volontairement une vérification de mise à jour système, une connexion PSN ou un téléchargement de firmware pour tester.

**Depuis un Mac :** `dig @127.0.0.1 ...` teste le DNS **du Mac**, pas celui de la PS5 ! Et `dig @<IP-LAN-PS5>` ne fonctionne normalement pas puisque nanoDNS n'écoute que l'adresse loopback de la console. Ne pas modifier `bind` en `0.0.0.0` juste pour faire ce test.

**Contrôle E :** blocage réellement observé dans les logs console ; ce n'est pas une preuve d'absence de connexion IP directe.

## 6 — Réactiver éventuellement Internet de manière SÉLECTIVE

**Seulement si tu acceptes les limites d'un filtrage DNS**, et si Eden Encore / tes homebrews ont besoin d'accéder à des services extérieurs :

1. Vérifier encore une fois que nanoDNS **tourne**, que la dernière session affiche **124 règles / 0 exception** et que les **deux DNS console** sont `127.0.0.1`.
2. Retirer la restriction WAN **uniquement en acceptant que des domaines non listés, des adresses IP directes et des résolveurs alternatifs puissent communiquer**. Si « aucune fuite, même par IP » est obligatoire, **laisser le pare-feu/WAN fermé**.
3. Tester un accès **autorisé** : une fonctionnalité homebrew qui utilise `github.com` ou des métadonnées publiques non bloquées.
4. Chercher dans les logs la requête correspondante et une réponse **upstream via `1.1.1.1` ou `9.9.9.9`**. Une application qui fonctionne avec son cache ne valide pas à elle seule la résolution.
5. Continuer à surveiller les requêtes bloquées et les domaines inattendus. Ne jamais utiliser un test de mise à jour système comme preuve.

**Contrôle F :** domaines ciblés bloqués, domaine autorisé effectivement résolu, risques résiduels compris.

## 7 — Après un reboot, crash ou retour du mode repos

- nanoDNS est un **payload en mémoire** ; après un **redémarrage complet**, le relancer (sauf autostart réellement vérifié après cold boot).
- Avec **les deux DNS à `127.0.0.1`**, la résolution classique ne fonctionne généralement pas **tant que nanoDNS n'est pas lancé**. Ce « fail-closed » DNS ne bloque **pas** les communications IP directes ou alternatives.
- **Routine recommandée :** WAN externe bloqué → démarrer console/loader local → lancer nanoDNS → relire les premiers logs → contrôler les 2 DNS → vérifier des requêtes bloquées → éventuellement rouvrir Internet sous risque accepté.
- Après une sortie du **mode repos**, vérifier que le processus écoute toujours et que de nouvelles requêtes apparaissent.
- Pour toute modification future de `nanodns.ini` : transférer → redémarrer le payload → revérifier les premiers logs → contrôler une requête bloquée et une requête autorisée.

## 8 — Diagnostic, retour arrière et maintenance

| Symptôme | Réaction conseillée **avec WAN bloqué** |
| --- | --- |
| Pas de connexion après redémarrage | Relancer nanoDNS ; les DNS loopback ne fonctionnent pas sans lui. |
| `config loaded` ne montre pas 124 règles / 0 exception | Restaurer le bon fichier `nanodns.ini`, relancer ; maximum 128 règles. |
| Aucun `query from` après modification | Vérifier les deux champs DNS et produire une requête bénigne depuis un outil **sur la console**, si disponible. |
| Un domaine Sony obtient une vraie IP publique | Laisser WAN bloqué et vérifier résolveur, cache, exceptions et correspondance des règles. |
| Test Internet / PSN de la console échoue | C'est compatible avec le blocage volontaire de Sony ; utiliser un service tiers autorisé pour diagnostiquer. |
| Un service légitime ne fonctionne plus | Vérifier les règles larges `*sony*`, `*nintendo*` et `a192.d.akamai.net`. |
| Impossible de lancer le loader hors ligne | **Ne pas supposer la protection garantie.** Préparer un accès local ou un pare-feu extérieur. |
| Retour arrière nécessaire | **WAN bloqué**, restaurer `nanodns.ini.bak`, relancer le payload ; changer les DNS console seulement en comprenant les risques. |

**Maintenance :** nanoDNS v0.4 réécrit son fichier de logs **à chaque lancement**. Sauvegarder le journal avant de redémarrer si l'on veut conserver les traces. Les tentatives répétées `AAAA` sur PSN n'indiquent pas nécessairement un défaut. Masquer les données personnelles des logs partagés publiquement.

**Note importante :** des mises à jour déjà téléchargées peuvent être installées sans aucun DNS ; désactiver leur installation automatique reste indispensable. Une liste DNS sélective n'empêche pas non plus un jeu/émulateur d'utiliser une IP en dur.

## Checklist finale — « Be safe »

- [ ] Premier chargement effectué **sans WAN**.
- [ ] Sauvegarde de la configuration.
- [ ] `/data/nanodns/nanodns.ini` chargé sans erreur : **124 règles / 0 exception**.
- [ ] Loader + nanoDNS actifs, écoute sur `127.0.0.1:53`.
- [ ] **DNS principal et secondaire : `127.0.0.1`**.
- [ ] Logs **après changement DNS** : requête interceptée, A→`0.0.0.0`, AAAA→0 réponse.
- [ ] Mises à jour automatiques et téléchargements en attente examinés.
- [ ] Si Internet sélectif activé : test d'un domaine autorisé + upstream dans les logs.
- [ ] Routine après redémarrage connue, limites du DNS acceptées ; si **zéro fuite exigée**, restriction WAN conservée.

**À lire également :** [couverture](COVERAGE.md) · [modèle de sécurité](THREAT_MODEL.md) · [nanoDNS upstream](https://github.com/drakmor/nanoDNS).
