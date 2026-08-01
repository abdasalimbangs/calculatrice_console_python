
def lire_choix(choix_valides):

    choix = int(input("Votre choix : "))

    while choix not in choix_valides:
        print("Choix invalide")
        choix = int(input("Nouveau choix  : "))

    return choix



