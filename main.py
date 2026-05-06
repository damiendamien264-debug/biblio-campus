from menu import afficher_menu

if __name__ == "__main__":
    while True:
        afficher_menu()
        choix = input("Choix : ")
        if choix == "4":
            print("Au revoir !")
            break
        elif choix in ("1", "2", "3"):
            print("Fonctionnalité en cours de développement...\n")
        else:
            print("Choix invalide.\n")