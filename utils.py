# Importações
from services import *


# Funções
def encerrar_programa() -> None:
    print("Finalizando programa...")
    exit()

def exibir_menu() -> None:
    print("\n--- Menu ---")
    [print(f"{indice}. {admin_menu_opcao['opcao']}") for indice, admin_menu_opcao in enumerate(admin_menu_opcoes, 1)]


# Constantes
admin_menu_opcoes = [
    {
        "opcao": "Buscar cursos por campus",
        "handler": buscar_cursos_por_campus
    },
    {
        "opcao": "Buscar cursos por tipo de curso",
        "handler": buscar_cursos_por_tipo
    },
    {
        "opcao": "Buscar cursos por nome",
        "handler": buscar_cursos_por_nome
    },
    {
        "opcao": "Cadastrar novo curso",
        "handler": cadastrar_novo_curso
    },
    {
        "opcao": "Sair",
        "handler": encerrar_programa
    }
]

