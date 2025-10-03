import bibliotheque
import exceptions
import models

repertoire = bibliotheque.BibliothequeAvecFichiers("Bibliothèque")


#########################################################   EXECUTION DES FONCTIONS ################################################################

livre1 = models.LivreNumerique("Le labyrinthe", "je sais pu", "243-415", 20)   
livre2 = models.LivreNumerique("Rainbow Six", "Tom Clancy", "843-484", 50)

repertoire.ajout_livre(livre1)
repertoire.ajout_livre(livre2)

repertoire.rechercher()

repertoire.exporter_csv()
repertoire.export_json()

erreurFichiers = exceptions.ErreurBibliotheque()
erreurFichiers.testFichier()
