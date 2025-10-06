class Livre:
    def __init__(self, titre: str, auteur: str, ISBN: str):
        self.titre = titre
        self.auteur = auteur
        self.ISBN = ISBN
    
class LivreNumerique(Livre):
    def __init__(self, titre: str, auteur: str, ISBN: str, taille: int):
        self.taille = taille
        self.auteur = auteur
        self.ISBN = ISBN
        self.titre = titre


class Bibliotheque:
    def __init__(self, nom: str):
        self.nom = nom
        self.liste_livres = []
    
    def ajout_livre(self, livre):
        self.liste_livres.append(livre)

    def rechercher(self, ISBN: str):
        liste_resultat = []
        for i in self.liste_livres:
            if i.ISBN == ISBN:
                print(i)
                liste_resultat.append(i)
        return liste_resultat

    def __len__(self):
        return len(self.liste_livres)