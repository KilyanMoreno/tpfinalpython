class ErreurBibliotheque(Exception):
    def __init__(self, ):
        super().__init__()

    def testFichier(self):
        try:
            fichier = open("./docs/data.json")
        except FileNotFoundError:
            print("Chef ton ficher existe pas")
        except PermissionError:
            print("Permission refusée")
        else:
            print("Ouverture du fichier JSON complété")
        finally:
            fichier.close()

        try:
            fichier = open("./docs/output.csv")
        except FileNotFoundError:
            print("Le ficher existe pas")
        except PermissionError:
            print("Permission refusée")
        else:
            print("Ouverture du fichier CSV terminé")
        finally:
            fichier.close()


