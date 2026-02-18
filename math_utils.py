def es_par(n: int) -> bool:
    """Retorna True si n es un número par, False en caso contrario."""
    return n % 2 == 0

def es_multiplo_de(n: int, m: int) -> bool:
    """
    Retorna True si n es múltiplo de m, False en caso contrario.
    Si m es 0, retorna False para evitar división por cero.
    """
    if m == 0:
        return False
    return n % m == 0