import json
from pathlib import Path

# Fichier JSON où seront stockés les mots de passe hachés
FICHIER_MOTS_DE_PASSE = Path("passwords.json")


def charger_mots_de_passe():
    """
    Charge les mots de passe depuis le fichier JSON.
    Retourne un dict {service: hash}.
    """
    if not FICHIER_MOTS_DE_PASSE.exists():
        return {}

    try:
        with FICHIER_MOTS_DE_PASSE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        # Fichier corrompu ou vide
        return {}

    # On attend un dictionnaire {service: hash}
    if isinstance(data, dict):
        return data
    # Si ce n'est pas le cas (ancien format, etc.) → on repart sur quelque chose de propre
    return {}


def sauvegarder_mots_de_passe(mots_de_passe: dict):
    """
    Sauvegarde le dict {service: hash} dans le fichier JSON.
    """
    with FICHIER_MOTS_DE_PASSE.open("w", encoding="utf-8") as f:
        json.dump(mots_de_passe, f, indent=2, ensure_ascii=False)


def ajouter_mot_de_passe_hache(service: str, hash_mdp: str):
    """
    Ajoute un mot de passe haché associé à un service.
    Empêche :
      - d'écraser un service déjà existant,
      - d'enregistrer deux fois le même mot de passe (même hash) pour un autre service.

    Retourne (ok: bool, message: str).
    """
    service = service.strip()
    mots_de_passe = charger_mots_de_passe()

    # 1) Un mdp existe déjà pour ce service
    if service in mots_de_passe:
        return False, f"Un mot de passe est déjà enregistré pour le service « {service} »."

    # 2) Même hash déjà enregistré pour un autre service
    if hash_mdp in mots_de_passe.values():
        return False, "Ce mot de passe est déjà enregistré pour un autre service."

    # 3) Tout est OK → on enregistre
    mots_de_passe[service] = hash_mdp
    sauvegarder_mots_de_passe(mots_de_passe)
    return True, f"Mot de passe enregistré pour le service « {service} »."


def afficher_mots_de_passe():
    """
    Affiche en console les mots de passe hachés enregistrés, organisés par service.
    """
    mots_de_passe = charger_mots_de_passe()

    if not mots_de_passe:
        print("\nAucun mot de passe enregistré pour le moment.")
        return

    print("\nMots de passe enregistrés (SERVICE : hash SHA-256 du MDP) :")
    for i, (service, h) in enumerate(mots_de_passe.items(), start=1):
        print(f"{i}. {service} : {h}")


def vider_mots_de_passe():
    """
    Supprime tous les mots de passe enregistrés
    en réécrivant le fichier JSON avec un dict vide.
    """
    sauvegarder_mots_de_passe({})