# =============================================================
# stats.py — Tableau de bord et statistiques de la bibliothèque
# Auteur : Collaborateur C
# Rôle   : Calculer et afficher des indicateurs statistiques
#          sur l'état actuel de la bibliothèque
# =============================================================

from books import books  # On importe la liste globale des livres


def afficher_stats():
    """
    Calcule et affiche un tableau de bord simple avec :
    - le nombre total de livres,
    - le nombre de livres disponibles,
    - le nombre de livres actuellement empruntés,
    - le taux de disponibilité en pourcentage.
    """

    total = len(books)  # Nombre total de livres dans la bibliothèque

    if total == 0:
        # Cas particulier : bibliothèque vide
        print("\n📊 Aucun livre enregistré dans la bibliothèque.")
        return

    # Compte les livres dont le champ "disponible" vaut True
    disponibles = len([b for b in books if b["disponible"]])

    # Les empruntés sont simplement ceux qui ne sont pas disponibles
    empruntes = total - disponibles

    # Calcul du pourcentage de disponibilité (arrondi à 1 décimale)
    taux = round((disponibles / total) * 100, 1)

    print("\n========== 📊 Tableau de bord ==========")
    print(f"  Total de livres      : {total}")
    print(f"  Livres disponibles   : {disponibles}")
    print(f"  Livres empruntés     : {empruntes}")
    print(f"  Taux de disponibilité: {taux}%")
    print("=========================================")


def livre_le_plus_emprunte():
    """
    Fonction bonus — Retourne le titre du livre le moins disponible.
    (Dans une version avancée, on stockerait un compteur d'emprunts.)
    Pour l'instant, retourne simplement le premier livre emprunté trouvé.

    Retourne :
        str : Le titre du livre emprunté, ou un message si aucun
    """
    for livre in books:
        if not livre["disponible"]:
            return livre["titre"]
    return "Tous les livres sont disponibles."
