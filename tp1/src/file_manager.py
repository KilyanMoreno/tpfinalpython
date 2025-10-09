import pickle
import csv
import json
from src import models


class BibliothequeAvecFichiers(models.Bibliotheque):
    def __init__(self, nom):
        super().__init__(nom)
        self.nom = nom
        self.liste_livres = []
        self.list_dict_books = []

    def exporter_csv (self):
        
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









