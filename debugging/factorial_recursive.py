#!/usr/bin/python3
import sys #import de la bibliothèque pr argv

def factorial(n): #déclaration d'un fonction
    if n == 0: #si n est strictement égal à 0
        return 1 #on retourne 1
    else: #sinon
        return n * factorial(n - 1) #on exécute la récursive

if len(sys.argv) < 2: #on vérifie si il y a au moins deux arguments passé
    #sinon message d'erreur
    print("Usage: ./factorial_recursive.py <non-negative integer>")
    sys.exit(1) #sortie du programme

try: #vérifie si l'argument est un entier
    n = int(sys.argv[1])
except ValueError: #si pas un entier renvoie un message d'erreur
    print("Error: Please provide a valid integer.")
    sys.exit(1) #sortie du programme

if n < 0: #vérifie si n est inférieur à 0
    #si inférieur renvoie un message d'erreur
    print("Error: Factorial is not defined for negative numbers.")
    sys.exit(1) #sortie du programme

f = factorial(n) #fait appel à la fonction
print(f) #print le résultat dans la console
