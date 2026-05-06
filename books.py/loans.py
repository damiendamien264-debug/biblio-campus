# =============================================================
# loans.py — Gestion des emprunts et retours de livres
# Auteur : Collaborateur C
# Rôle   : Modifier le statut de disponibilité d'un livre
#          lors d'un emprunt ou d'un retour
# =============================================================


def emprunter_livre(livre):
    """
    Enregistre l'emprunt d'un livre si celui-ci est disponible.

    Paramètre :
        livre (dict) : Le dictionnaire représentant le livre à emprunter

    Retourne :
        bool : True si l'emprunt a réussi, False si le livre était déjà emprunté
    """
    if livre["disponible"]:
        # On marque le livre comme non disponible
        livre["disponible"] = False
        return True   # Emprunt enregistré avec succès
    return False       # Livre déjà emprunté, opération impossible


def rendre_livre(livre):
    """
    Enregistre le retour d'un livre emprunté.
    Le livre redevient disponible pour un autre emprunt.

    Paramètre :
        livre (dict) : Le dictionnaire représentant le livre à rendre
    """
    # On remet le statut disponible à True, quel que soit l'état actuel
    livre["disponible"] = True
