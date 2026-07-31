# Étape 1 : Cahier des charges

Le cahier des charges est le document qui décrit ce que le client veut, sans parler de technique.
# Contexte

Une petite entreprise souhaite une calculatrice en ligne de commande pour ses employés.

Cette calculatrice devra être simple à utiliser, fiable et évolutive.

À terme, l'entreprise souhaite pouvoir ajouter des fonctionnalités comme :

un historique des calculs ;
des statistiques ;
de nouvelles opérations ;
une sauvegarde des calculs.

La première version doit donc être conçue pour évoluer facilement.

# Objectif

Développer une application permettant à un utilisateur de :

réaliser des opérations mathématiques de base ;
obtenir un résultat immédiatement ;
continuer à effectuer plusieurs calculs sans relancer le programme

# Fonctionnalités de la version 1.0

# Notre MVP (Minimum Viable Product) comprendra :

# Fonctionnalité	Version 1.0
Addition	✅
Soustraction	✅
Multiplication	✅
Division	✅
Quitter l'application	✅

# Les fonctionnalités suivantes seront développées plus tard :

Historique
Mémoire
Sauvegarde
Calcul scientifique
Export

# Architecture MVP

├── calculator
│   ├── app.py
│   ├── history.py
│   ├── menu.py
│   ├── operation.py
│   ├── test
│   └── validator.py
└── README.md

3 directories, 6 files