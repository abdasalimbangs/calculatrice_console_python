# import
import menu
import validator
import operations

# initialisation 
CHOIX_VALIDES = [0, 1, 2, 3, 4]
choix = -1

# Controle pour afficher le menu et lire le choix 
while choix != 0:

    menu.afficher_menu()
    choix = validator.lire_choix(CHOIX_VALIDES)

    # Controle pour faire addition si le choix est égale à 1
    if choix == 1:

        resultat = operations.effectuer_addition()
        print(f" Resultat : {resultat}" )
    # Controle pour faire la soustraction si le choix est égale à 2
    elif choix == 2 : 
        resultat = operations.effectuer_soustraction()
        print(f"Resultat : {resultat}")
    # Controle pour faire le produit si le choix est égale à 3
    elif choix == 3 : 
        resultat = operations.effectuer_multiplication()
        print(f"Resultat : {resultat}")
    # Controle pour faire le produit si le choix est égale à 4
    elif choix == 4 : 

        resultat = operations.effectuer_division()
        if resultat is None:
        print("Division impossible : le diviseur ne peut pas être zéro.")
        
        print(f"Resultat : {resultat}")