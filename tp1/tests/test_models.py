import pytest
import json

def test_rechercher(biblioaveclivres):
    resultats = biblioaveclivres.rechercher("243-415")

    assert len(resultats) == 1
    livre_trouve = resultats[0]
    assert livre_trouve.titre == "Le labyrinthe"

def tester_add_livre(biblioVide, livre_py):
    biblioVide.ajout_livre(livre_py)

    assert len(biblioVide) >= 1


def tester_add_livre_num(biblioVide, livre_num_py):
    biblioVide.ajout_livre(livre_num_py)
    assert len(biblioVide) >= 1


def test_exportfichiers(export_folders, list_dict_books):
    with open('./docs/data.json', 'w') as f:
        json.dump(list_dict_books, f, indent=2)
