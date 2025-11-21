import hashlib

CARACTERES_SPECIAUX = "!@#$%^&*"

def valider_mot_de_passe(mot_de_passe: str):
    """
    Vérifie que le mot de passe respecte toutes les règles.
    Retourne (True, []) si tout va bien,
    ou (False, [liste de messages d'erreurs]).
    """
    erreurs = []

    # Règle 1 : longueur
    if len(mot_de_passe) < 8:
        erreurs.append("Le mot de passe doit contenir au moins 8 caractères.")
    # Règle 2 : au moins une majuscule
    if not any(c.isupper() for c in mot_de_passe):
        erreurs.append("Le mot de passe doit contenir au moins une lettre majuscule.")
    # Règle 3 : au moins une minuscule
    if not any(c.islower() for c in mot_de_passe):
        erreurs.append("Le mot de passe doit contenir au moins une lettre minuscule.")
    # Règle 4 : au moins un chiffre
    if not any(c.isdigit() for c in mot_de_passe):
        erreurs.append("Le mot de passe doit contenir au moins un chiffre.")
    # Règle 5 : au moins un caractère spécial
    if not any(c in CARACTERES_SPECIAUX for c in mot_de_passe):
        erreurs.append(f"Le mot de passe doit contenir au moins un caractère spécial : {CARACTERES_SPECIAUX}")

    # True si aucune erreur, False sinon
    est_valide = len(erreurs) == 0
    return est_valide, erreurs

def hacher_mot_de_passe(mot_de_passe: str) -> str:
    """
    Retourne le hash SHA-256 du mot de passe, sous forme de chaîne hexadécimale.
    """
    # 1) convertir en bytes
    mot_de_passe_bytes = mot_de_passe.encode("utf-8")

    # 2) calculer le hash
    hash_obj = hashlib.sha256(mot_de_passe_bytes)

    # 3) renvoyer la représentation hexadécimale
    return hash_obj.hexdigest()