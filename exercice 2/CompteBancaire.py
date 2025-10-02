class CompteCancaire:
    def __init__(self, titulaire: str, solde_initial: float = 0):
        self.titulaire = "kilyan"
        self.solde_initial = 0
        self.solde = 0
        print("Solde initial :", self.solde_initial)
        pass

    def deposer(self, montant: float):
        self.solde = self.solde_initial
        self.solde = self.solde + montant
        print ("Ajout de :", montant)
        print("Montant total après opération :", self.solde)
        pass

    def retirer(self, montant: float):
        self.solde = self.solde - montant
        print("retrait de :", montant)
        print("Montant total compte :", self.solde)
        pass


compte = CompteCancaire("Kilyan", 0)

compte.deposer(500)
compte.retirer (200)

print(compte.solde)



class Vehicule:
    def __init__(self, marque: str):
        self.marque = marque

class Voiture(Vehicule):
    def __init__(self, marque: str, portes: int):
        super().__init__(marque)
        self.portes = portes
        print("Il y a : ", portes, "portes")

class Motos(Vehicule):
     def __init__(self, marque: str, moteur: int):
        super().__init__(marque)
        self.moteur = moteur
        print("La moto est une :", moteur, "c3")


Moto1 = Motos("Honda", 125)
Voiture1 = Voiture("Ford", 5)


