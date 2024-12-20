from repositories.professor import *
from . import exibir_lista_objeto, admin_menu_opcoes, tables, eh_indice_valido, obter_id_de_lista, exibir_menu_atualizar_deletar, visualizar_detalhes, cores
from repositories.curso import find_curso_by_id, find_all_cursos

def exibir_menu_professor():
    """Funções CRUD para professores"""
    print(f"{cores['azul']}\nMenu Professores{cores['reset']}")

    crud_opcoes = admin_menu_opcoes[tables["professor"]]["crud_opcoes"]
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

    professores = []
    if escolha == "1":
        professores = buscar_professores()
    elif escolha == "2":
        professores = [buscar_professor_por_nome()]
    elif escolha == "3":
        professores = buscar_professores_por_curso()
    elif escolha == "4":
        cadastrar_novo_professor()

    if len(professores) > 0:
        id_professor_resposta = obter_id_de_lista(professores)
        if (id_professor_resposta["sucesso"]):
            opcao = exibir_menu_atualizar_deletar()
            if opcao == 1:
                atualizar_professor(id_professor_resposta["_id"])
            elif opcao == 2:
                remover_professor(id_professor_resposta["_id"])

    exibir_menu_professor()

# Funções CRUD para professores

def cadastrar_novo_professor():
    """Função para cadastrar um novo professor."""
    nome_professor = input("Digite o nome do professor: ").strip()
    while not nome_professor:
        print(f"{cores['vermelho']}Nome inválido. Tente novamente.{cores['reset']}")
        nome_professor = input("Digite o nome do professor: ").strip()

    departamento = input("Digite o departamento do professor: ").strip()
    while not departamento:
        print(f"{cores['vermelho']}Departamento inválido. Tente novamente.{cores['reset']}")
        departamento = input("Digite o departamento do professor: ").strip()

    email_professor = input("Digite o e-mail do professor: ").strip()
    while not email_professor:
        print(f"{cores['vermelho']}E-mail inválido. Tente novamente.{cores['reset']}")
        email_professor = input("Digite o e-mail do professor: ").strip()

    professor = {
        "nome_professor": nome_professor,
        "departamento": departamento,
        "email_professor": email_professor
    }

    resultado = inserir_novo_professor(professor)
    if resultado.acknowledged:
        print(f"{cores['verde']}Professor {nome_professor} cadastrado com sucesso!{cores['reset']}")
        return professor
    else:
        print(f"{cores['vermelho']}Erro ao cadastrar professor.{cores['reset']}")
        return {}

def buscar_professores():
    professores = find_all_professores()
    professores_lista = list(professores)
    if professores_lista:
        print("\nProfessores encontrados:")
        exibir_lista_objeto(professores_lista)
        return professores_lista
    else:
        print(f"{cores['vermelho']}Nenhum professor encontrado.{cores['reset']}")
        return []


def buscar_professores_por_curso():
    """Busca professores por curso."""
    curso_id = input("Digite o ID do curso para buscar seus professores: ").strip()
    curso = find_curso_by_id(curso_id)
    if not curso:
        print(f"{cores['vermelho']}Nenhum curso encontrado.{cores['reset']}")
        return []
    professores = find_professores_by_curso(curso_id)
    if not professores:
        print(f"{cores['vermelho']}Nenhum professor encontrado.{cores['reset']}")
        return []
    
    professores_lista = list(professores)
    
    if professores_lista:
        print(f"Professores encontrados para o curso: {curso['nome_curso']}")
        exibir_lista_objeto(professores_lista)
        return professores_lista
    return []

def buscar_professor_por_nome():
    """Busca professor por nome."""
    nome_professor = input("Digite o nome do professor: ").strip()
    while not nome_professor:
        print(f"{cores['vermelho']}O nome é necessário. Tente novamente.{cores['reset']}")
        nome_professor = input("Digite o nome do professor: ").strip()
    professor = find_professor_by_nome(nome_professor)

    if professor:
        print(f"Professor encontrado: {professor['nome_professor']}")
        exibir_lista_objeto([professor])
        return professor
    else:
        print(f"{cores['vermelho']}Professor não encontrado.{cores['reset']}")
        return {'_id': None}

def atualizar_professor(id_professor):
    """Atualiza os dados do professor."""
    professor_encontrado = find_professor_by_id(id_professor)
    print("Detalhes atuais do professor:")
    visualizar_detalhes(professor_encontrado)

    novos_dados = {}

    nome_professor = input("Digite o novo nome do professor (deixe em branco para manter o atual): ").strip()
    if nome_professor:
        novos_dados["nome_professor"] = nome_professor

    departamento = input("Digite o novo departamento (deixe em branco para manter o atual): ").strip()
    if departamento:
        novos_dados["departamento"] = departamento

    email_professor = input("Digite o novo e-mail (deixe em branco para manter o atual): ").strip()
    if email_professor:
        novos_dados["email_professor"] = email_professor

    todos_cursos = find_all_cursos()
    if todos_cursos:
        cursos_list = list(todos_cursos)
        if len(cursos_list) > 0:
            print("\nEscolha os cursos:")
            for i, curso in enumerate(cursos_list, 1):
                print(f"{i}. {curso['nome_curso']}")

            selecionados = input("Digite os números dos cursos separados por vírgula (deixe em branco para manter os atuais): ").strip().split(",")
            while not (all(eh_indice_valido(selecionado, len(cursos_list)) for selecionado in selecionados) or selecionados == ['']):
                print(f"{cores['vermelho']}Ao menos um dos números é inválido. Tente novamente.{cores['reset']}")
                selecionados = input("Digite os números dos cursos separados por vírgula (deixe em branco para manter os atuais): ").strip().split(",")
            
            if selecionados != ['']:
                novos_dados['cursos'] = [cursos_list[int(selecionado) - 1]["_id"] for selecionado in selecionados]

    if novos_dados:
        atualizar_professor_no_banco(id_professor, novos_dados)
        return novos_dados
    else:
        print(f"{cores['verde']}Nenhum dado foi atualizado.{cores['reset']}")
        return {}

def remover_professor(id_professor):
    """Remove um professor do banco."""
    professor_encontrado = find_professor_by_id(id_professor)
    print(f"{cores['vermelho']}Você está prestes a excluir o professor '{professor_encontrado['nome_professor']}'.{cores['reset']}")
    confirmar = input("Tem certeza? [S/N]: ").strip().lower()
    if len(confirmar) > 0 and confirmar[0] == 's':
        remover_professor_do_banco(id_professor)
    else:
        print(f"{cores['verde']}Deleção cancelada.{cores['reset']}")
