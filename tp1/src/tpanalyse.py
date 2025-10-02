etudiants = [
    {"nom": "alice", "note": 15, "annee": 2},
    {"nom": "félix", "note": 20, "annee": 1},
    {"nom": "gérard", "note": 9, "annee": 2},
    {"nom": "jean", "note": 3, "annee": 2},
    {"nom": "alex", "note": 8, "annee": 3},
    {"nom": "paul", "note": 12, "annee": 4},
    {"nom": "germain", "note": 0, "annee": 1},
    {"nom": "jeffe", "note": 19, "annee": 4}

]

mentions_ab = []
mentions_b = []


# question 1
for etudiant in etudiants:
    if etudiant["note"] >=12:
        print("admis :", [etudiant])

#question 3
    if  15 <= etudiant["note"] < 18:
        mentions_ab.append(etudiant["nom"])
        mentions_ab.append(etudiant["note"])
        mentions_ab.append(["mention assez bien"])
    if etudiant["note"] >=18:
        mentions_b.append(etudiant["nom"])
        mentions_b.append(etudiant["note"])
        mentions_b.append(["mention bien"])

#correcion question 3

def calcul_mention(note):
    seuil_mentions = [
        (17, "très bien")
        (15, "bien")
        (12, "ok tier")
        (8, "dehors")
    ]
    for seuil, mention in seuil_mentions:
        if note >= seuil:
            return mention
        
etudiants_sorted = sorted(etudiants, key = lambda x:["note"], reverse = True)
mentions = (etudiant["nom"]: calcul_mention(etudiant["note"]) for etudiant in etudiants_sorted))

# voir fichier correction

print(mentions_ab)
print(mentions_b)

####################

moyenne = sorted(etudiants, key=lambda x: x["note"])
annee = sorted(moyenne, key=lambda x: x["annee"])

