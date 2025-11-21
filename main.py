from securisation import valider_mot_de_passe, hacher_mot_de_passe

def main():
    while True:
        mot_de_passe = input("\nChoisissez un mot de passe : ")

        est_valide, erreurs = valider_mot_de_passe(mot_de_passe)

        if est_valide:
            print("\nMot de passe valide !")
            break
        else:
            print("\nMot de passe invalide :", end="\n")
            for e in erreurs:
                print(" -", e)
            print("\nVeuillez réessayer.\n")

    # Une fois le mot de passe valide → hash
    hash_mdp = hacher_mot_de_passe(mot_de_passe)
    print("\nHash SHA-256 du mot de passe :", end=" ")
    print(hash_mdp, end="\n\n")


if __name__ == "__main__":
    main()