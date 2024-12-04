# utils.py

from services import *
from constants import admin_menu_opcoes, tables, cores

from services.curso import exibir_menu_curso
from services.semestre import exibir_menu_semestre
from services.professor import exibir_menu_professor

# Funções
def encerrar_programa() -> None:
    print(f"{cores['vermelho']}Finalizando programa...{cores['reset']}")
    exit()

def exibir_menu() -> None:
    print(f"{cores['azul']}\n--- Menu principal ---{cores['reset']}")
    indice = 1
    for key, value in admin_menu_opcoes.items():
        print(f"{indice}. {value['opcao']}")
        indice += 1
    print(f"{cores['vermelho']}0. Encerrar programa{cores['reset']}")


def executar_crud(table):
    """Função para executar o CRUD baseado na tabela."""
    if table == tables["curso"]:
        exibir_menu_curso()
    elif table == tables["semestre"]:
        exibir_menu_semestre()
    elif table == tables["professor"]:
        exibir_menu_professor()
    else:
        print(f"{cores['vermelho']}Tabela não reconhecida.{cores['reset']}")