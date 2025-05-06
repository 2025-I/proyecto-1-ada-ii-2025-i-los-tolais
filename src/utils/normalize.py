def normalize(s: str) -> str:
    """
    Convierte a minúsculas y elimina todo lo que no sea letra o dígito.
    """
    return "".join(ch.lower() for ch in s if ch.isalnum())
