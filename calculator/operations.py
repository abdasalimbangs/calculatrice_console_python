import inputs

# Fonction pour le calcul pur de l'addition
def addition(a, b):
    return a + b

# Fonction pour le calcul pur de la soustraction
def soustraction(a, b):
    return a - b

# Fonction pour le calcul pur du produit
def multiplication(a, b):
    return a * b

# Fonction pour le calcul pur de la division
def division(a, b):
    if b == 0:
        return None
    return a / b

# Fonction pour interaction avec l'utilisateur
def effectuer_addition():
    nombre1,nombre2 = inputs.lire_deux_nombres()
    return addition(nombre1, nombre2)

# Fonction pour interaction avec l'utilisateur
def effectuer_soustraction():
    nombre1,nombre2 = inputs.lire_deux_nombres()
    return soustraction(nombre1, nombre2)

# Fonction pour interaction avec l'utilisateur
def effectuer_multiplication():
    nombre1,nombre2 = inputs.lire_deux_nombres()
    return multiplication(nombre1, nombre2)

# Fonction pour interaction avec l'utilisateur
def effectuer_division():
    nombre1,nombre2 = inputs.lire_deux_nombres()
    resultat = division(nombre1, nombre2)
    return resultat
