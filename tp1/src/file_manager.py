import pickle
import csv
import json
import models


class BibliothequeAvecFichiers(models.Bibliotheque):
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
        
        with open('./tp1/docs/output.csv', 'w', newline='',
            encoding='utf-8') as file:
            writer = csv.DictWriter(file,
            fieldnames=['titre', 'auteur', "ISBN", "taille"])
            writer.writeheader()
            writer.writerows(self.list_dict_books)
        
        return(f"titre : {livre.titre}, auteur : {livre.auteur}, ISBN : {livre.ISBN}, taille : {livre.taille}ko")

    def export_json(self):

        with open('./tp1/docs/data.json', 'w') as f:
            json.dump(self.list_dict_books, f, indent=2)

        with open('./tp1/docs/data.json', 'r') as f:
            self.list_dict_books = json.load(f)









