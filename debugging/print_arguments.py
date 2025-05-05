#!/usr/bin/python3
import sys #import bibliothèque pour argv

#si la length des arguments est inférieure à 2
if len(sys.argv) < 2:
    #on print un message d'erreur
    print("Usage: ./print_args.py <arg1> <arg2> ...")
    sys.exit(1) #on quitte le programme

#sinon on boucle en partant de l'argument[1]
for i in range(1, len(sys.argv)):
    print(sys.argv[i]) #on print l'argument
