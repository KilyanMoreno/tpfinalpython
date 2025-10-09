import pytest
import json
import tempfile
import os
from tp1.src.models import Bibliotheque, LivreNumerique
from tp1.src.file_manager import BibliothequeAvecFichiers

class ErreurBibliotheque(Exception):
    pass

class BibliothequeAvecFichiers(Bibliotheque):
    def export_json(self, chemin):
        try:
            dossier = os.path.dirname(chemin)
            if dossier and not os.path.exists(dossier):
                os.makedirs(dossier)

            data = [
                {
                    "titre": livre.titre,
                    "auteur": livre.auteur,
                    "isbn": livre.ISBN,
                    "taille": livre.taille,
                }
                for livre in self.liste_livres
            ]

            with open(chemin, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)

        except Exception as e:
            raise ErreurBibliotheque(f"Erreur lors de la sauvegarde JSON : {e}")

    def import_json(self, chemin):
        if not os.path.exists(chemin):
            raise ErreurBibliotheque("Fichier JSON introuvable")

        try:
            with open(chemin, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, list):
                raise ErreurBibliotheque("Structure JSON invalide")

            self.liste_livres = [
                LivreNumerique(
                    item["titre"], item["auteur"], item["ISBN"], item["taille"]
                )
                for item in data
            ]

        except json.JSONDecodeError:
            raise ErreurBibliotheque("Fichier JSON invalide")
        except Exception as e:
            raise ErreurBibliotheque(f"Erreur lors du chargement JSON : {e}")

    def exporter_csv(self, chemin):
        try:
            dossier = os.path.dirname(chemin)
            if dossier and not os.path.exists(dossier):
                os.makedirs(dossier)

            with open(chemin, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Titre", "Auteur", "ISBN", "Taille"])
                for livre in self.liste_livres:
                    writer.writerow(
                        [livre.titre, livre.auteur, livre.ISBN, livre.taille]
                    )

        except PermissionError:
            raise ErreurBibliotheque("Permission refusée pour écrire le CSV")
        except Exception as e:
            raise ErreurBibliotheque(f"Erreur lors de l'export CSV : {e}")
        

def test_sauvegarde_chargement_cycle():
    biblio = BibliothequeAvecFichiers("Test")
    biblio.ajout_livre(LivreNumerique("Livre A", "Auteur X", "123", 200))
    biblio.ajout_livre(LivreNumerique("Livre B", "Auteur Y", "456", 300))

    with tempfile.TemporaryDirectory() as tmpdir:
        chemin = os.path.join(tmpdir, "data.json")
        biblio.export_json(chemin)

        biblio2 = BibliothequeAvecFichiers("Test import")
        biblio2.import_json(chemin)

        assert len(biblio2.liste_livres) == 2
        assert biblio2.liste_livres[0].titre == "Livre A"


def test_sauvegarde_repertoire_inexistant():
    biblio = BibliothequeAvecFichiers("Test")
    biblio.ajout_livre(LivreNumerique("Livre A", "Auteur X", "123", 200))

    chemin = os.path.join("un_dossier_qui_n_existe_pas", "data.json")

    # Doit créer automatiquement le dossier
    biblio.export_json(chemin)
    assert os.path.exists(chemin)
    os.remove(chemin)
    os.rmdir("un_dossier_qui_n_existe_pas")


def test_chargement_fichier_inexistant():
    biblio = BibliothequeAvecFichiers("Test")
    with pytest.raises(ErreurBibliotheque):
        biblio.import_json("fichier_inexistant.json")


def test_chargement_fichier_invalide():
    with tempfile.TemporaryDirectory() as tmpdir:
        chemin = os.path.join(tmpdir, "data.json")
        # fichier avec contenu non JSON
        with open(chemin, "w") as f:
            f.write("{invalide:}")

        biblio = BibliothequeAvecFichiers("Test")
        with pytest.raises(ErreurBibliotheque):
            biblio.import_json(chemin)


def test_chargement_fichier_structure_invalide():
    with tempfile.TemporaryDirectory() as tmpdir:
        chemin = os.path.join(tmpdir, "data.json")
        with open(chemin, "w", encoding="utf-8") as f:
            json.dump({"titre": "Mauvais format"}, f)

        biblio = BibliothequeAvecFichiers("Test")
        with pytest.raises(ErreurBibliotheque):
            biblio.import_json(chemin)


def test_export_csv_complet():
    biblio = BibliothequeAvecFichiers("Test CSV")
    biblio.ajout_livre(LivreNumerique("Livre A", "Auteur X", "123", 200))
    biblio.ajout_livre(LivreNumerique("Livre B", "Auteur Y", "456", 300))

    with tempfile.TemporaryDirectory() as tmpdir:
        chemin = os.path.join(tmpdir, "export.csv")
        biblio.exporter_csv(chemin)

        assert os.path.exists(chemin)

        with open(chemin, "r", encoding="utf-8") as f:
            contenu = f.read()
            assert "Livre A" in contenu
            assert "Livre B" in contenu


def test_export_csv_erreur_permission(monkeypatch):

    def faux_open(*args, **kwargs):
        raise PermissionError("Accès refusé")

    biblio = BibliothequeAvecFichiers("Test")
    biblio.ajout_livre(LivreNumerique("Livre A", "Auteur X", "123", 200))

    with tempfile.TemporaryDirectory() as tmpdir:
        chemin = os.path.join(tmpdir, "fichier.csv")

        monkeypatch.setattr("builtins.open", faux_open)

        with pytest.raises(ErreurBibliotheque):
            biblio.exporter_csv(chemin)
