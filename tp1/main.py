import sys, os
# Ajoute la racine du projet (tp1) dans le PYTHONPATH
sys.path.append(os.path.dirname(__file__))
from src import file_manager 
from src import exceptions
from src import models

repertoire = file_manager.BibliothequeAvecFichiers("Bibliothèque")


#########################################################   EXECUTION DES FONCTIONS ################################################################

livre1 = models.LivreNumerique("Le labyrinthe", "je sais pu", "243-415", 20)   
livre2 = models.LivreNumerique("Rainbow Six", "Tom Clancy", "843-484", 50)

repertoire.ajout_livre(livre1)
repertoire.ajout_livre(livre2)
repertoire.rechercher("884-445")


repertoire.exporter_csv()
repertoire.export_json()


erreurs = exceptions.ErreurBibliotheque()
erreurs.testFichier()

