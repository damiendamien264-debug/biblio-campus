def ajouter_livre(titre, auteur, isbn=""):
    data = charger_donnees()
    livre = {
        "titre": titre,
        "auteur": auteur,
        "isbn": isbn,
        "disponible": True
    }
    data["livres"].append(livre)
    sauvegarder_donnees(data)
    return livre

def lister_livres():
    data = charger_donnees()
    return data["livres"]

def rechercher_livre(terme):
    data = charger_donnees()
    resultats = []
    for livre in data["livres"]:
        if terme.lower() in livre["titre"].lower() or terme.lower() in livre["auteur"].lower():
            resultats.append(livre)
    return resultats

def supprimer_livre(titre):
    data = charger_donnees()
    data["livres"] = [l for l in data["livres"] if l["titre"] != titre]
    sauvegarder_donnees(data)
