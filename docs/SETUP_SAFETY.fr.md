# Démarrage et sécurité réseau

**Langues :** [English (default)](SETUP_SAFETY.md) | Français

La politique est **sélective** : les noms non répertoriés restent résolus par les DNS amont Control D puis AdGuard DNS, sans filtrage supplémentaire lorsqu'un nanoDNS actif reçoit la requête.

## Risque au premier démarrage

Un fichier `nanodns.ini` enregistré ne protège pas la console avant l'exécution du payload. Le chargeur, le système ou une application peuvent exploiter un cache, une IP directe ou un autre DNS. Pour une protection stricte, **bloquer le WAN depuis un routeur/pare-feu externe** (IPv4 et IPv6), tout en conservant l'accès LAN au chargeur.

Procédure : démarrage hors WAN → chargeur local → nanoDNS → lecture du journal → DNS console primaire et secondaire `127.0.0.1` → vérification de requêtes effectivement bloquées → ouverture sélective éventuelle du WAN, si les risques résiduels sont acceptés.

Après un redémarrage complet, un crash ou une reprise, revérifier que le processus et les écouteurs sont actifs. Ne pas réutiliser un journal de la veille comme preuve.

## Ce que les logs prouvent

- `124 rule(s), 0 exception(s)` : le profil prévu a été chargé.
- `listening on 127.0.0.1:53` : un écouteur local existe à cet instant.
- `override matched` : la requête DNS observée a été interceptée.
- Une réponse amont Control D ou AdGuard pour un domaine autorisé indique que cette résolution a fonctionné.

Aucun de ces signaux ne garantit que toutes les connexions IP, tous les domaines ou les mises à jour sont bloqués.

Voir le [guide français](INSTALL.fr.md), le [guide anglais](INSTALL.md) et le [modèle de risque](THREAT_MODEL.fr.md).
