import pickle
import csv
import json

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
   
    def exporter_csv (self):
        self.list_dict_books = []
        
        for livre in self.liste_livres:
            self.list_dict_books.append({
                "titre": livre.titre,
                "auteur": livre.auteur,
                "ISBN": livre.ISBN,
                "taille": livre.taille
            }) 
            print(self.list_dict_books)
        
        with open('./docs/output.csv', 'w', newline='',
            encoding='utf-8') as file:
            writer = csv.DictWriter(file,
            fieldnames=['titre', 'auteur', "ISBN", "taille"])
            writer.writeheader()
            writer.writerows(self.list_dict_books)
        
        return(f"titre : {livre.titre}, auteur : {livre.auteur}, ISBN : {livre.ISBN}, taille : {livre.taille}ko")

    def export_json(self):

        with open('./docs/data.json', 'w') as f:
            json.dump(self.list_dict_books, f, indent=2)

        with open('./docs/data.json', 'r') as f:
            self.list_dict_books = json.load(f)


repertoire = Bibliotheque("Bibliothèque")

livre1 = LivreNumerique("Le labyrinthe", "je sais pu", "243-415", 20)   
livre2 = LivreNumerique("Rainbow Six", "Tom Clancy", "843-484", 50)

repertoire.ajout_livre(livre1)
repertoire.ajout_livre(livre2)

repertoire.rechercher()

repertoire.exporter_csv()
repertoire.export_json()