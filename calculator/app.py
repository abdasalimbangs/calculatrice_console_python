# import
import menu
import validator

# initialisation 
CHOIX_VALIDES = [0, 1, 2, 3, 4]
choix = -1

while choix != 0:
    menu.afficher_menu()
    choix = validator.lire_choix(CHOIX_VALIDES)
    print(choix)