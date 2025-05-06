#!/usr/bin/python3

def print_board(board):  # Fonction d'affichage du plateau
    print("  0   1   2")  # En-tête de colonne
    for idx, row in enumerate(board):  # On parcourt chaque ligne du plateau
        print(idx, " | ".join(row))  # On affiche la ligne avec des séparateurs visuels
        if idx < 2:
            print("  " + "-" * 9)  # On ajoute une ligne de séparation sauf après la dernière ligne

def check_winner(board):  # Fonction qui vérifie s’il y a un gagnant
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # Retourne le symbole gagnant (X ou O)

    for col in range(len(board[0])):  # Vérifie les colonnes
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    # Diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  # Aucun gagnant

def is_full(board):  # Fonction qui vérifie si le plateau est rempli (égalité)
    for row in board:
        if " " in row:  # Si une case vide est encore présente
            return False
    return True

def tic_tac_toe():  # Fonction principale du jeu
    board = [[" "]*3 for _ in range(3)]  # Création d’un plateau 3x3 vide
    player = "X"  # Le joueur X commence

    while True:  # Boucle de jeu principale
        print_board(board)  # Affiche le plateau

        try:
            # Demande la ligne et la colonne
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in [0,1,2] or col not in [0,1,2]:
                print("Invalid coordinates. Try 0, 1, or 2.")
                continue  # Recommence la boucle si la saisie est hors limites
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue  # Recommence si la saisie n’est pas un nombre

        if board[row][col] != " ":  # Vérifie si la case est déjà prise
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player  # Place le symbole du joueur sur la case choisie

        winner = check_winner(board)  # Vérifie si le joueur a gagné
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")  # Affiche le gagnant
            break  # Fin du jeu

        if is_full(board):  # Si le plateau est plein sans gagnant
            print_board(board)
            print("It's a tie!")  # Match nul
            break  # Fin du jeu

        # Change de joueur pour le tour suivant
        player = "O" if player == "X" else "X"

tic_tac_toe()  # Appel de la fonction pour lancer le jeu
