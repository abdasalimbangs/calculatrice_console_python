import menu
import validator


choix = -1

while choix != 0:
    menu.afficher_menu()
    choix = validator.lire_choix()
    print(choix)