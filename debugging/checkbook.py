#!/usr/bin/python3

class Checkbook: #création d'une class nommée Checkbook
    def __init__(self): #initialisation de la class
        self.balance = 0.0 #sa balance est un float à zéro

    def deposit(self, amount): #fonction pour ajouter une valeur dans balance
        if amount <= 0: #vérifie si le dépot est négatif ou égal à 0
            #si oui print un message d'erreur explicite
            print("Please enter a positive amount to deposit.")
            return #ne retourne rien mais sort de la fonction
        self.balance += amount #sinon on incrémente balance avec la valeur de amount
        print("Deposited ${:.2f}".format(amount)) #on print amount dans un message
        #on print la nouvelle valeur de balance dans un message
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount): #fonction pour retirer une valeur de balance
        if amount <= 0: #on vérifie si la valeur est négative ou égal à 0
            #si oui on print un message d'erreur explicite
            print("Please enter a positive amount to withdraw.")
            return #on sort de la fonction en ne retournant rien
        if amount > self.balance: #on vérifie si le retrait est supérieur à la valeur de balance
            #dans ce cas on print un message d'erreur explicite
            print("Insufficient funds to complete the withdrawal.")
        else: #sinon
            self.balance -= amount #on retire la valeur de amount à la valeur de balance
            print("Withdrew ${:.2f}".format(amount)) #on print la valeur retirée
            print("Current Balance: ${:.2f}".format(self.balance)) #on print la nouvelle valeur de balance

    def get_balance(self): #fonction pour récupérer la valeur actuelle de balance
        print("Current Balance: ${:.2f}".format(self.balance)) #on print la valeur de balance

def main(): #fonction main
    cb = Checkbook() #on crée un raccourcie de la class checkbook
    while True: #on boucle tant que c'est vrais...
        #on attend une entrée de l'utilisateur
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit': #si l'action est exit 
            break #on arrête la boucle et on sort
        elif action == 'deposit': #si l'action est un depot
            try: #on essaye de le convertir en float et on récupère la valeur
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount) #si ok appel la class pour gérer le dépot
            except ValueError: #sinon print un message d'erreur explicite
                print("Invalid input. Please enter a number.")
        elif action == 'withdraw': #si l'action est un retrait
            try: #on essaye de le convertir en float et on récupère la valeur
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount) #si ok appel la class pour gérer le dépot
            except ValueError: #sinon print un message d'erreur explicite
                print("Invalid input. Please enter a number.")
        elif action == 'balance': #si l'action est de demander la balance
            cb.get_balance() #on fait appel à la class
        else: #sinon on affiche un message d'erreur explicite
            print("Invalid command. Please try again.")

if __name__ == "__main__":  #vérifie si ce fichier est exécuté directement
    main()  #si oui, on appelle la fonction principale du programme
