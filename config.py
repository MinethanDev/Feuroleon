#################################################################
# Projet : Feuroléon                      Création : 21.09.2022 #
# Auteur : Minethan                         Fichier : config.py #
# Description : Bot Discord humoristique répondant "Feur" à un  #
#               message finissant par "Quoi", ainsi que         #
#               d'autres fonctionnalités                        #
# Version : 2.5                                                 #
#################################################################

#--------------------[ Token du bot
BOT_TOKEN = ""

#--------------------[ ID du compte dev
id_dev = 0

#--------------------[ Liste des "Quoi" possibles
liste_quoi = ["quoi", "koi", "tfk", "pk", "kwa", "qwa", "kuwa", "quwa"]

#--------------------[ Liste des réponses possibles pour /question
reps_question = ["Oui", "Non", "Peut-être", "Probablement", "Probablement pas", "Impossible", "Sûrement"]

#--------------------[ Liste des réponses possibles pour un message finissant en "quoi"
reps_feur = {
    1: ("**Feur !**", "assets/coiffeur.png", True),
    2: ("**-druplé !**", "assets/druple.png", False),
    3: ("**-rtz !**", "assets/quartz.png", False),
    4: ("**-drilatère !**", "assets/drilatere.png", False),
    5: ("**-rterback !**", "assets/rterback.png", False)
}
