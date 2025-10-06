import pytest
from src.models import Bibliotheque, Livre, LivreNumerique


@pytest.fixture
def bibliotheque_vide():
        return Bibliotheque("Bibliotheque Municipale")


@pytest.fixture
def livre_simple():
        return Livre("111-888")

@pytest.fixture
def bibliotheque_pleine(livre_simple, bibliotheque_vide):
        bibliotheque_vide.ajouter_livre(livre_simple)
        return bibliotheque_vide


@pytest.fixture
def biblioaveclivres():
    b = Bibliotheque("Bibliothèque")
    livre1 = Livre("Le labyrinthe", "je sais pu", "243-415")
    livre2 = Livre("Rainbow Six", "Tom Clancy", "843-484")
    b.ajout_livre(livre1)
    b.ajout_livre(livre2)
    return b

@pytest.fixture
def biblioVide():
        return Bibliotheque("Bibliothèque")
        

@pytest.fixture
def livre_py():
       return Livre("Test", "tests", "544-658")

@pytest.fixture
def livre_num_py():
        return LivreNumerique('Test2', "testt", "542-651", 52)