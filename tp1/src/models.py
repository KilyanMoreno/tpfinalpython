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
    
    def ajout_livre (self, livre):
        self.liste_livres.append(livre)

    def rechercher (self):
        liste_resultat = []
        for i in self.liste_livres:
            if i.ISBN == "843-484":
                print(i)
                liste_resultat.append(i)
        for livre in liste_resultat:
            print(f"titre : {livre.titre}, auteur : {livre.auteur}, ISBN : {livre.ISBN}, taille : {livre.taille}ko")
   


