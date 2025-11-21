from securisation import valider_mot_de_passe, hacher_mot_de_passe
from stockage import ajouter_mot_de_passe_hache, afficher_mots_de_passe, vider_mots_de_passe


def demander_mot_de_passe():
    """
    Boucle qui demande un mot de passe à l'utilisateur
    jusqu'à ce qu'il soit valide.
    Retourne le mot de passe (en clair).
    """
    while True:
        mot_de_passe = input("\nChoisissez un mot de passe : ")

        est_valide, erreurs = valider_mot_de_passe(mot_de_passe)

        if est_valide:
            print("\nMot de passe valide !")
            return mot_de_passe
        else:
            print("\nMot de passe invalide :")
            for e in erreurs:
                print(" -", e)
            print("Veuillez réessayer.\n")


def menu_principal():
    while True:
        print("\n=== Gestion des mots de passe ===")
        print("1. Ajouter un nouveau mot de passe")
        print("2. Afficher les mots de passe enregistrés")
        print("3. Vider tous les mots de passe")
        print("4. Quitter")

        choix = input("Votre choix : ").strip()

        if choix == "1":
            mdp = demander_mot_de_passe()
            hash_mdp = hacher_mot_de_passe(mdp)
            ajouter_mot_de_passe_hache(hash_mdp)
            print("\nMot de passe enregistré (hashé) avec succès.")

        elif choix == "2":
            afficher_mots_de_passe()

        elif choix == "3":
            # Double confirmation
            print("\nATTENTION : cette action va supprimer TOUS les mots de passe enregistrés.")
            confirm1 = input("Confirmer ? (o/N) : ").strip().lower()

            if confirm1 != "o":
                print("\nOpération annulée.")
                continue

            confirm2 = input('Tapez exactement "SUPPRIMER" pour confirmer : ').strip()

            if confirm2 == "SUPPRIMER":
                vider_mots_de_passe()
                print("\nTous les mots de passe ont été supprimés.")
            else:
                print("\nDeuxième confirmation incorrecte, opération annulée.")

        elif choix == "4":
            print("\nArret du gestionnaire de mot de passe. Au revoir.")
            break

        else:
            print("\nChoix invalide, veuillez réessayer.")


def main():
    menu_principal()


if __name__ == "__main__":
    main()