# 📄 Exercice de débogage : `factorial.py`

## 🔍 Problème initial

Le script `factorial.py` devait calculer la factorielle d’un nombre passé en argument, mais il contenait plusieurs erreurs :

1. **Boucle infinie** : la variable `n` n’était pas décrémentée dans la boucle `while`.
2. **Pas de vérification d’argument** : crash si aucun argument n’était fourni.
3. **Pas de gestion des entrées invalides** : crash si l’argument n’était pas un entier.
4. **Aucun message clair pour l’utilisateur** : pas d’aide ni d’exemple d’usage.
5. **Non-portabilité du shebang sous Windows** : présence de `^M` ou mauvais chemin d’interpréteur.

## ✅ Résultat final

Le script est désormais :

- Fonctionnel et sans boucle infinie.
- Protégé contre les mauvaises entrées grâce à `try/except`.
- Doté de messages explicites.
- Compatible avec différents environnements (Windows, WSL, Linux).
- Exécutable via `python factorial.py <number>` ou `./factorial.py <number>`.

## 🧪 Exemple d’utilisation

```bash
$ python factorial.py 5
120
