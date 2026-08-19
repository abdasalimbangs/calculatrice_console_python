# import
import menu
import validator
import operations

# initialisation 
CHOIX_VALIDES = [0, 1, 2, 3, 4]

# Creation de mapping
operations_map = {
    1: operations.effectuer_addition,
    2: operations.effectuer_soustraction,
    3: operations.effectuer_multiplication,
    4: operations.effectuer_division,
}

choix = -1

# Controle pour afficher le menu et lire le choix 
while choix != 0:

    menu.afficher_menu()
    choix = validator.lire_choix(CHOIX_VALIDES)

    if choix != 0 :
        # Nous pouvons récupérer la fonction
        operation = operations_map[choix]
        resultat = operation()
        if resultat is None :
            print("Division impossible : le diviseur ne peut pas être zéro.")
        else: 
            print(f"Résultat : {resultat}")

        