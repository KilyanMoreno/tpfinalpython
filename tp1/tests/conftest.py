import pytest
from src.models import Bibliotheque, Livre

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