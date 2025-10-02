import csv
import json



donnees = [
    {'titre': 'rainbow six', 'auteur': "tom clancy", "taille": 50},
    {'titre': 'le labyrinthe', 'auteur': "james dashner", "taille": 30}
]

with open('./docs/output.csv', 'w', newline='',
    encoding='utf-8') as file:
    writer = csv.DictWriter(file,
    fieldnames=['titre', 'auteur', "taille"])
    writer.writeheader()
    writer.writerows(donnees)

