# 🧪 Exercices de débogage Python, HTML & JavaScript

Ce dossier contient des scripts corrigés dans le cadre du projet **"Enhancing Code Quality and Efficiency with ChatGPT"**, visant à améliorer la robustesse, la lisibilité et l'efficacité du code dans plusieurs langages (Python, HTML, JavaScript).

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

## 📁 Script 2 : `print_args.py`

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
$ python print_args.py hello world
Arguments fournis :
hello
world
```

---

## 📁 Script 3 : `change_background.html`

### 🔍 Problème initial

Une faute de frappe dans l’attribut `id` du bouton empêchait le JavaScript de fonctionner (`colorButon` au lieu de `colorButton`).

### ✅ Corrections apportées

- Correction du nom d’`id` dans le bouton HTML (`colorButton`)
- Aucun besoin de déplacer le script, il était déjà placé après le DOM
- Conservation d’un JavaScript simple et lisible

### 🧪 Fonctionnement

- Lorsqu’on clique sur le bouton, une couleur aléatoire est générée et appliquée à l’arrière-plan du document.
- Fonctionne dans tous les navigateurs modernes.

---

## 📚 Objectif pédagogique

- Identifier rapidement les fautes de frappe classiques en HTML/JS
- S’assurer que le DOM est prêt avant exécution d’un script
- Travailler sur la logique événementielle simple
- Étendre les compétences de debugging à plusieurs langages du Web

---

## 📁 Script 4 : `minesweeper.py`

### 🔍 Problème initial

Le jeu fonctionnait partiellement, mais plusieurs erreurs logiques empêchaient une expérience correcte :
- Les coordonnées des mines étaient mal indexées (mauvais calcul des positions).
- Aucune vérification des entrées : le joueur pouvait faire planter le programme en sortant du plateau.
- Aucune détection de victoire : le jeu ne se terminait que si une mine était déclenchée.

### ✅ Corrections apportées

- Correction de la formule d’index `(y * width + x)` dans tout le code.
- Ajout d’un contrôle sur les coordonnées entrées par l’utilisateur.
- Ajout d’une méthode `is_victory()` pour détecter la fin de partie réussie.
- Maintien de l’affichage clair et du fonctionnement récursif sur les cases vides.

### 🧠 Remarque personnelle

Ce script utilise de la programmation orientée objet et de la manipulation d’index 2D avancée.  
Il sera commenté plus tard lorsque la formation m’aura permis de mieux maîtriser ces notions.

---
