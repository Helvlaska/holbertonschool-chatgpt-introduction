#!/usr/bin/python3
import sys #Import de bibliothèque (argv)

#déclaration de fonction : 
#def nom_variable(paramètre)
def factorial(n): 
    result = 1 #variable
    while n > 1: #tant que n > 1
        result *= n
        n -= 1 #décrémente n pour avancer dans la boucle
    return result #on renvoie le resultat

if len(sys.argv) < 2: #on vérifie qu’un argument utilisateur a bien été fourni
    print("Usage: ./factorial.py <positive integer>")
    print("Example: ./factorial.py 5  → will print 120 (because 5! = 120)")
    sys.exit(1)  #on arrête le programme proprement avec un code d'erreur

try: #on essaye de...
    n = int(sys.argv[1])  #... convertir argv[1] en entier
except ValueError: #si echec on print un message d'erreur
    print("Error: Please enter a valid positive integer")
    sys.exit(1)  #sortie propre si conversion échoue

if n < 0:
    print("Error: Please enter a *positive* integer only.")
    sys.exit(1)

#on utilise la fonction 
f = factorial(n) 
print(f) #on print le resultat
