def eh_indice_valido(indice: str, end: int, start: int = 1) -> bool:
    return indice.isdigit() and int(indice) >= start and int(indice) <= end