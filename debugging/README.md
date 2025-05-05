# 🧪 Exercices de débogage Python

Ce dossier contient des scripts corrigés dans le cadre du projet **"Enhancing Code Quality and Efficiency with ChatGPT"**, visant à améliorer la robustesse, la lisibilité et l'efficacité du code Python.

---

## 📁 Script 1 : `factorial.py`

### 🔍 Problème initial

Calcul incorrect ou infini de la factorielle d’un entier donné en argument.  
Plusieurs erreurs étaient présentes : boucle infinie, absence de vérifications, mauvaise gestion des entrées, etc.

### ✅ Corrections apportées

- Décrémentation de `n` dans la boucle `while`
- Vérification de la présence d’un argument utilisateur
- Conversion protégée par un `try/except`
- Message d’usage clair avec exemple
- Vérification que l’entier est positif
- Compatibilité avec Windows (résolution du problème `^M` et du shebang)

### 🧪 Exemple d’utilisation

```bash
$ python factorial.py 5
120
```

---

## 📁 Script 2 : `print_arguments.py`

### 🔍 Problème initial

Le script affichait tous les éléments de `sys.argv`, y compris le nom du fichier lui-même (`argv[0]`), ce qui n’était pas pertinent.  
Il n’y avait pas non plus de vérification en cas d'absence d'arguments.

### ✅ Corrections apportées

- La boucle commence à `1` pour ignorer `argv[0]`
- Ajout d’un message d’usage si aucun argument n’est fourni
- Utilisation de `sys.exit(1)` pour une sortie propre
- Code structuré et commenté pour favoriser la compréhension

### 🧪 Exemple d’utilisation

```bash
$ python print_arguments.py hello world
Arguments fournis :
hello
world
```

---

## 📚 Objectif pédagogique

- Identifier les erreurs classiques liées à `sys.argv`
- Travailler sur les bonnes pratiques de contrôle des entrées utilisateur
- Structurer son code avec des conditions, des boucles, et des messages clairs
- Appliquer des standards professionnels dans des scripts simples

---
