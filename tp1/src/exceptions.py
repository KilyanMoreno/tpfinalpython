class ErreurBibliotheque(Exception):
    def __init__(self, message="Erreur lors du chargement de la bibliothèque"):
        super().__init__(message)

    def testFichier(self):
        try:
            fichier = open("./docs/data.json")
            fichier.close()
        except FileNotFoundError:
            print("Chef ton ficher existe pas")
        except PermissionError:
            print("Permission refusée")
        else:
            print("Ouverture du fichier JSON complété")

        try:
            fichier = open("./docs/output.csv")
            fichier.close()
        except FileNotFoundError:
            print("Le ficher existe pas")
        except PermissionError:
            print("Permission refusée")
        else:
            print("Ouverture du fichier CSV terminé")
