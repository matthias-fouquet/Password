import json
from pathlib import Path

# Fichier JSON où seront stockés les mots de passe hachés
FICHIER_MOTS_DE_PASSE = Path("passwords.json")


def charger_mots_de_passe():
    """
    Charge la liste des mots de passe hachés depuis le fichier JSON.
    Retourne une liste de chaînes (hashs).
    """
    if not FICHIER_MOTS_DE_PASSE.exists():
        return []

    try:
        with FICHIER_MOTS_DE_PASSE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        # Fichier corrompu ou vide
        return []

    if isinstance(data, list):
        return data
    return []


def sauvegarder_mots_de_passe(mots_de_passe):
    """
    Sauvegarde la liste des mots de passe hachés dans le fichier JSON.
    """
    with FICHIER_MOTS_DE_PASSE.open("w", encoding="utf-8") as f:
        json.dump(mots_de_passe, f, indent=2, ensure_ascii=False)


def ajouter_mot_de_passe_hache(hash_mdp: str):
    """
    Ajoute un mot de passe haché dans le fichier.
    (Phase 3 : on pourra ici gérer les doublons.)
    """
    mots_de_passe = charger_mots_de_passe()
    mots_de_passe.append(hash_mdp)
    sauvegarder_mots_de_passe(mots_de_passe)


def afficher_mots_de_passe():
    """
    Affiche en console la liste des mots de passe hachés enregistrés.
    """
    mots_de_passe = charger_mots_de_passe()

    if not mots_de_passe:
        print("\nAucun mot de passe enregistré pour le moment.")
        return

    print("\nMots de passe enregistrés (hash SHA-256) :")
    for i, h in enumerate(mots_de_passe, start=1):
        print(f"{i}. {h}")

def vider_mots_de_passe():
    """
    Supprime tous les mots de passe enregistrés
    en réécrivant le fichier JSON avec une liste vide.
    """
    sauvegarder_mots_de_passe([])