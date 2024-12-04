from repositories.semestre import *
from . import exibir_lista_objeto, admin_menu_opcoes, tables, eh_indice_valido, obter_id_de_lista, exibir_menu_atualizar_deletar, visualizar_detalhes, cores
from repositories.curso import find_all_cursos

def exibir_menu_semestre():
    """Funções CRUD para semestres"""
    print(f"{cores['azul']}\nMenu semestre{cores['reset']}")

    crud_opcoes = admin_menu_opcoes[tables["semestre"]]["crud_opcoes"]
    for indice, opcao in enumerate(crud_opcoes, 1):
        print(f"{indice}. {opcao}")
    
    escolha = input("Escolha uma opção (deixe vazio para retornar): ").strip().lower()
    while not (eh_indice_valido(escolha, len(crud_opcoes)) or escolha == ""):
        print(f"{cores['vermelho']}Opção inválida! Tente novamente.{cores['reset']}")
        for indice, opcao in enumerate(crud_opcoes, 1):
            print(f"{indice}. {opcao}")
        escolha = input("Escolha uma opção (deixe vazio para retornar): ").strip().lower()

    if escolha == "":
        return

    semestres = []
    if escolha == "1":
        semestres = buscar_semestres()
    elif escolha == "2":
        cadastrar_novo_semestre()
    
    if len(semestres) > 0:
        id_semestre_resposta = obter_id_de_lista(semestres)
        if (id_semestre_resposta["sucesso"]):
            opcao = exibir_menu_atualizar_deletar()
            if opcao == 1:
                atualizar_semestre(id_semestre_resposta["_id"])
            elif opcao == 2:
                deletar_semestre(id_semestre_resposta["_id"])

    exibir_menu_semestre()

# Funções CRUD para semestres

def cadastrar_novo_semestre():
    """Função para cadastrar um novo semestre."""
    ano = input("Digite o ano do semestre: ").strip()
    while not (ano.isdigit() and int(ano) >= 1500):
        print(f"{cores['vermelho']}Ano inválido. Tente novamente.{cores['reset']}")
        ano = input("Digite o ano do semestre: ").strip()

    numero_semestre = input("Digite o número do semestre (ex: 1 ou 2): ").strip()
    while numero_semestre not in ["1", "2"]:
        print(f"{cores['vermelho']}Número do semestre inválido. Tente novamente.{cores['reset']}")
        numero_semestre = input("Digite o número do semestre (ex: 1 ou 2): ").strip()

    status = input("Digite o status do semestre (ex: 'ativo', 'encerrado', 'cancelado'): ").strip()
    while status not in ["ativo", "encerrado", "cancelado"]:
        print(f"{cores['vermelho']}Status inválido. Tente novamente.{cores['reset']}")
        status = input("Digite o status do semestre (ex: 'ativo', 'encerrado', 'cancelado'): ").strip()

    semestre = {
        "ano": int(ano),
        "numero_semestre": int(numero_semestre),
        "status": status
    }

    resultado = inserir_novo_semestre(semestre)
    if resultado.acknowledged:
        print(f"{cores['verde']}Semestre {ano}/{numero_semestre} cadastrado com sucesso!{cores['reset']}")
        return semestre
    else:
        print(f"{cores['vermelho']}Erro ao cadastrar semestre.{cores['reset']}")
        return {}

def buscar_semestres() -> list[any]:
    """Busca todos os semestres."""
    semestres = find_all_semestres()
    semestres_lista = list(semestres)

    if semestres_lista:
        print("Semestres encontrados:")
        exibir_lista_objeto(semestres_lista)
        return semestres_lista
    else:
        print(f"{cores['vermelho']}Nenhum semestre encontrado.{cores['reset']}")
        return []


def buscar_semestres_por_status():
    """Busca semestres por status."""
    status = input("Digite o status do semestre (ex: 'ativo', 'encerrado', 'cancelado'): ").strip()
    while status not in ["ativo", "encerrado", "cancelado"]:
        print(f"{cores['vermelho']}Status inválido. Tente novamente.{cores['reset']}")
        status = input("Digite o status do semestre (ex: 'ativo', 'encerrado', 'cancelado'): ").strip()
    semestres = find_semestre_by_status(status)
    semestres_lista = list(semestres)

    if semestres_lista:
        print(f"Semestres encontrados com status '{status}':")
        exibir_lista_objeto(semestres_lista)
        return semestres_lista
    else:
        print(f"{cores['vermelho']}Nenhum semestre encontrado com status '{status}'.{cores['reset']}")
        return []

def atualizar_semestre(id_semestre):
    """Atualiza os dados de um semestre."""
    semestre_encontrado = find_semestre_by_id(id_semestre)
    print("Detalhes atuais do semestre:")
    visualizar_detalhes(semestre_encontrado)

    novos_dados = {}

    ano = input("Digite o ano do semestre (deixe em branco para manter o atual): ").strip()
    while not ((ano.isdigit() and int(ano) >= 1500) or ano == ""):
        print(f"{cores['vermelho']}Ano inválido. Tente novamente.{cores['reset']}")
        ano = input("Digite o ano do semestre (deixe em branco para manter o atual): ").strip()

    if ano:
        novos_dados["ano"] = int(ano)

    numero_semestre = input("Digite o número do semestre (ex: 1 ou 2, ou deixe em branco para manter o atual): ").strip()
    while (numero_semestre != "" and numero_semestre not in ["1", "2"]):
        print(f"{cores['vermelho']}Número do semestre inválido. Tente novamente.{cores['reset']}")
        numero_semestre = input("Digite o número do semestre (ex: 1 ou 2 ou deixe em branco para manter o atual): ").strip()

    if numero_semestre:
        novos_dados["numero_semestre"] = int(numero_semestre)

    status = input("Digite o status do semestre (ex: 'ativo', 'encerrado', 'cancelado' ou deixe em branco para manter o atual): ").strip()
    while status != "" and (status not in ["ativo", "encerrado", "cancelado"]):
        print(f"{cores['vermelho']}Status inválido. Tente novamente.{cores['reset']}")
        status = input("Digite o status do semestre (ex: 'ativo', 'encerrado', 'cancelado' ou deixe em branco para manter o atual): ").strip()

    todos_cursos = find_all_cursos()
    if todos_cursos:
        cursos = list(todos_cursos)
        if len(cursos) > 0:
            print("\nEscolha os cursos:")
            for i, curso in enumerate(cursos, 1):
                print(f"{i}. {curso['nome_curso']}")
                
            selecionados = input("Digite os números dos cursos separados por vírgula (deixe em branco para manter os atuais): ").strip().split(",")
            while not (all(eh_indice_valido(selecionado, len(cursos)) for selecionado in selecionados) or selecionados == ['']):
                print(f"{cores['vermelho']}Ao menos um dos números é inválido. Tente novamente.{cores['reset']}")
                selecionados = input("Digite os números dos cursos separados por vírgula (deixe em branco para manter os atuais): ").strip().split(",")
            
            if selecionados != ['']:
                novos_dados['cursos'] = [cursos[int(selecionado) - 1]["_id"] for selecionado in selecionados]

    if status:
        novos_dados["status"] = status

    if novos_dados:
        atualizar_semestre_no_banco(id_semestre, novos_dados)
        return novos_dados
    else:
        print(f"{cores['verde']}Nenhum dado novo foi fornecido para atualização.{cores['reset']}")
        return {}

def deletar_semestre(id_semestre):
    """Remove um semestre."""
    semestre_encontrado = find_semestre_by_id(id_semestre)
    print(f"{cores['vermelho']}Você está prestes a excluir o semestre '{semestre_encontrado['ano']}/{semestre_encontrado['numero_semestre']}'.{cores['reset']}")
    confirmar = input("Tem certeza? [S/N]: ").strip().lower()
    if len(confirmar) > 0 and confirmar[0] == 's':
        remover_semestre_do_banco(id_semestre)
    else:
        print(f"{cores['verde']}Deleção cancelada.{cores['reset']}")
