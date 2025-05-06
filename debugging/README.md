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

## 📁 Script 5 : `factorial_recursive.py`

### 🔍 Problème initial

Le script calcule bien la factorielle d’un entier en mode récursif, mais il manquait plusieurs sécurités :
- Pas de vérification de l’argument (crash si rien n’est passé)
- Pas de gestion des entrées invalides (texte ou négatif)
- Aucune aide utilisateur ni message clair

### ✅ Corrections apportées

- Ajout d’une vérification du nombre d’arguments
- Conversion en entier protégée par `try/except`
- Rejet des entiers négatifs avec message explicite
- Affichage clair d’un message d’usage si mal utilisé
- Fonction récursive conservée sans modification de logique

### 🧪 Exemple d’utilisation

```bash
$ python factorial_recursive.py 4
24
```

---

## 📁 Script 6 : `checkbook.py`

### 🔍 Problème initial

Le script permettait d’effectuer des dépôts, des retraits et de consulter un solde, mais il contenait plusieurs failles :
- Aucune gestion d’erreur sur la saisie utilisateur → crash si texte au lieu d’un montant
- Possibilité de déposer ou retirer des montants négatifs
- Pas de tolérance sur les espaces ou majuscules dans les commandes

### ✅ Corrections apportées

- Entourer les saisies numériques avec un `try/except` pour éviter les `ValueError`
- Rejeter les montants ≤ 0 dans les méthodes `deposit()` et `withdraw()`
- Utiliser `.strip().lower()` sur les entrées pour fiabiliser les commandes
- Messages utilisateur clairs et pédagogiques

### 🧪 Exemple d’utilisation

```bash
$ python checkbook.py
What would you like to do? (deposit, withdraw, balance, exit): deposit
Enter the amount to deposit: $50
Deposited $50.00
Current Balance: $50.00
```

---

## 📁 Script 7 : `tic_tac_toe.py`

### 🔍 Problème initial

Ce jeu de morpion fonctionnait, mais plusieurs bugs ou oublis de logique nuisaient à son bon déroulement :
- Le joueur déclaré vainqueur n’était pas le bon (affiché après changement de tour)
- Aucune détection d’égalité lorsque le plateau était rempli
- Aucune gestion d’erreur sur les entrées utilisateur (texte, nombres hors plage)
- Affichage du plateau peu lisible

### ✅ Corrections apportées

- Réécriture de `check_winner()` pour retourner le vrai gagnant
- Ajout de la fonction `is_full()` pour détecter une égalité
- Protection des saisies utilisateur avec `try/except` et vérification de plage
- Amélioration de l’affichage avec des indices de ligne et colonne

### 🧪 Exemple d’utilisation

```bash
$ python tic_tac_toe.py
  0   1   2
0   |   |  
  ---------
1   |   |  
  ---------
2   |   |  

Enter row (0, 1, or 2) for player X: 1
Enter column (0, 1, or 2) for player X: 1
...
Player X wins!
```

---
