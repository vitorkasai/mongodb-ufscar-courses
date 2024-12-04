# utils.py

from services import *
from constants import admin_menu_opcoes, tables

from services.curso import exibir_menu_curso
from services.semestre import exibir_menu_semestre
from services.professor import exibir_menu_professor

# Funções
def encerrar_programa() -> None:
    print("Finalizando programa...")
    exit()

def exibir_menu() -> None:
    print("\n--- Menu ---")
    indice = 1
    for key, value in admin_menu_opcoes.items():
        print(f"{indice}. {value['opcao']}")
        indice += 1
    print("0. Encerrar programa")


def executar_crud(table):
    """Função para executar o CRUD baseado na tabela."""
    if table == tables["curso"]:
        exibir_menu_curso()
    elif table == tables["semestre"]:
        exibir_menu_semestre()
    elif table == tables["professor"]:
        exibir_menu_professor()
    else:
        print("Tabela não reconhecida.")