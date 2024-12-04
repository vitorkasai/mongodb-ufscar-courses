from bson import ObjectId

from constants import cores
from helpers import eh_indice_valido


# Função genérica para exibir listas
def exibir_lista(dados):
    print("-" * 30)
    for i, item in enumerate(dados, 1):
        print(f"{i}. {item}")


def exibir_lista_objeto(dados):
    for item in dados:
        visualizar_detalhes(item)


def visualizar_detalhes(dados):
    print("-" * 30)
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


def obter_id_de_lista(dados: list[any]):
    """Obtém um id de uma lista de dados."""
    id_selecionado = input(f"\nEscolha um '_id' para manipular (deixe vazio para voltar): ").strip()
    try:
        id_selecionado_obj = ObjectId(id_selecionado)
    except Exception:
        id_selecionado_obj = None

    ids = [dado['_id'] for dado in dados]

    while id_selecionado != "" and str(id_selecionado_obj) not in [str(id) for id in ids]:
        print(f"{cores['vermelho']}'_id' inválido! Tente novamente.{cores['reset']}")
        id_selecionado = input(f"\nEscolha um '_id' para manipular (deixe vazio para voltar): ").strip()
        try:
            id_selecionado_obj = ObjectId(id_selecionado)
        except Exception:
            id_selecionado_obj = None

    if id_selecionado == "":
        return {'sucesso': False, '_id': None}
    return {'sucesso': True, '_id': id_selecionado_obj}


def exibir_menu_atualizar_deletar() -> int:
    """Função para retornar a opção de atualizar ou deletar um certo dado. Ou -1 se deixado vazio."""
    print(f"{cores['azul']}\nMenu de atualização e remoção{cores['reset']}")
    print(f"{cores['laranja']}1. Atualizar{cores['reset']}")
    print(f"{cores['vermelho']}2. Deletar{cores['reset']}")

    escolha = input("Escolha uma opção (deixe vazio para voltar): ").strip().lower()
    while not (eh_indice_valido(escolha, 2) or escolha == ""):
        print(f"{cores['vermelho']}Opção inválida! Tente novamente.{cores['reset']}")
        print(f"{cores['azul']}\nMenu de atualização e remoção{cores['reset']}")
        print(f"{cores['laranja']}1. Atualizar{cores['reset']}")
        print(f"{cores['vermelho']}2. Deletar{cores['reset']}")
        escolha = input("Escolha uma opção (deixe vazio para voltar): ").strip().lower()

    if escolha == "":
        return -1
    return int(escolha)
