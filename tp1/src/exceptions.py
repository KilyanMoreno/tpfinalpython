class ErreurBibliotheque(Exception):
    def __init__(self, message="Erreur lors du chargement de la bibliothèque"):
        super().__init__(message)

    def testFichier(self):
        try:
            fichier = open("./tp1/docs/data.json")
        except FileNotFoundError:
            print("Chef ton ficher existe pas")
        except PermissionError:
            print("Permission refusée")
        else:
            print("Ouverture du fichier JSON complété")
        finally:
            fichier.close()

        try:
            fichier = open("./tp1/docs/output.csv")
        except FileNotFoundError:
            print("Le ficher existe pas")
        except PermissionError:
            print("Permission refusée")
        else:
            print("Ouverture du fichier CSV terminé")
        finally:
            fichier.close()


