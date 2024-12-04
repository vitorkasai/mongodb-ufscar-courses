from repositories.curso import *
from . import visualizar_detalhes, eh_indice_valido, admin_menu_opcoes, tables, exibir_lista_objeto, obter_id_de_lista, exibir_menu_atualizar_deletar, cores
from repositories.semestre import find_all_semestres
from repositories.professor import find_professor_by_id, find_all_professores


def exibir_menu_curso():
    """Funções CRUD para cursos"""
    print(f"{cores['azul']}\nMenu Curso{cores['reset']}")
    crud_opcoes = admin_menu_opcoes[tables["curso"]]["crud_opcoes"]
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

    cursos = []
    if escolha == "1":
        cursos = buscar_cursos_por_campus()
    elif escolha == "2":
        cursos = buscar_cursos_por_tipo()
    elif escolha == "3":
        cursos = buscar_cursos_por_nome()
    elif escolha == "4":
        cursos = buscar_cursos_por_semestre()
    elif escolha == "5":
        cursos = buscar_cursos_por_professor()
    elif escolha == "6":
        cadastrar_novo_curso()
    
    if len(cursos) > 0:
        id_curso_resposta = obter_id_de_lista(cursos)
        if (id_curso_resposta["sucesso"]):
            opcao = exibir_menu_atualizar_deletar()
            if opcao == 1:
                atualizar_curso(id_curso_resposta["_id"])
            elif opcao == 2:
                deletar_curso(id_curso_resposta["_id"])

    exibir_menu_curso()

# Funções CRUD para cursos
def cadastrar_novo_curso():
    """Função para cadastrar um novo curso."""
    nome_curso = input("Digite o nome do curso: ").strip()
    while not nome_curso:
        print(f"{cores['vermelho']}Nome do curso é obrigatório.{cores['reset']}")
        nome_curso = input("Digite o nome do curso: ").strip()

    campus_list = find_all_campus()

    print("\nEscolha um campus:")
    for i, campus in enumerate(campus_list, 1):
        print(f"{i}. {campus}")

    campus_curso = input("Escolha o número do campus: ").strip()
    while not eh_indice_valido(campus_curso, len(campus_list)):
        print(f"{cores['vermelho']}Opção inválida! Tente novamente.{cores['reset']}")
        campus_curso = input("Escolha o número do campus: ").strip()


    tipo_list = find_all_tipo_curso()
    print("\nEscolha um tipo de curso:")
    for i, tipo in enumerate(tipo_list, 1):
        print(f"{i}. {tipo}")
    
    tipo_curso = input("Escolha o número do tipo de curso: ").strip()
    while not eh_indice_valido(tipo_curso, len(tipo_list)):
        print(f"{cores['vermelho']}Opção inválida! Tente novamente.{cores['reset']}")
        tipo_curso = input("Escolha o número do tipo de curso: ").strip()


    vagas_curso = input("Digite o número de vagas: ").strip()
    while not (vagas_curso.isdigit() and int(vagas_curso) >= 0):
        print(f"{cores['vermelho']}Número de vagas inválido. Digite um número inteiro maior ou igual a 0.{cores['reset']}")
        vagas_curso = input("Digite o número de vagas: ").strip()

    curso = {
        "nome_curso": nome_curso,
        "campus_curso": campus_list[int(campus_curso) - 1],
        "tipo_curso": tipo_list[int(tipo_curso) - 1],
        "vagas_curso": int(vagas_curso)
    }

    resultado = inserir_novo_curso(curso)
    if resultado.acknowledged:
        print(f"{cores['verde']}Curso '{nome_curso}' cadastrado com sucesso!{cores['reset']}")
        return curso
    else:
        print(f"{cores['vermelho']}Erro ao cadastrar curso.{cores['reset']}")
        return {}

def buscar_cursos_por_professor():
    """Busca cursos por professor."""
    professor_id = input("Digite o ID do professor para buscar cursos: ").strip()
    professor = find_professor_by_id(professor_id)
    if not professor:
        print(f"{cores['vermelho']}Nenhum professor encontrado.{cores['reset']}")
        return []
    cursos = find_cursos_by_professor(professor_id)
    if not cursos:
        print(f"{cores['vermelho']}Nenhum curso encontrado.{cores['reset']}")
        return []
    
    cursos_lista = list(cursos)
    
    if cursos_lista:
        print(f"Cursos encontrados para o professor: {professor['nome_professor']}")
        exibir_lista_objeto(cursos_lista)
        return cursos_lista
    return []

def buscar_cursos_por_semestre():
    """Busca cursos por semestre."""
    semestres = find_all_semestres()
    if not semestres:
        print(f"{cores['vermelho']}Nenhum semestre encontrado.{cores['reset']}")
        return []
    
    semestres_list = list(semestres)
    print("\nEscolha um semestre:")
    for i, semestre in enumerate(semestres_list, 1):
        print(f"{i}. {semestre['ano']}/{semestre['numero_semestre']}")

    escolha_semestre = input("Escolha o número do semestre: ").strip()
    while not eh_indice_valido(escolha_semestre, len(semestres_list)):
        print(f"{cores['vermelho']}Opção inválida! Tente novamente.{cores['reset']}")
        escolha_semestre = input("Escolha o número do semestre: ").strip()
    
    semestre = semestres_list[int(escolha_semestre) - 1]
    cursos = find_curso_by_semestre(semestre["_id"])
    cursos_lista = list(cursos)
    
    if cursos_lista:
        print(f"Cursos encontrados para o semestre: {semestre}")
        exibir_lista_objeto(cursos_lista)
        return cursos_lista
    else:
        print(f"{cores['vermelho']}Nenhum curso encontrado para o semestre '{semestre}'.{cores['reset']}")
        return []


def buscar_cursos_por_campus():
    """Busca cursos por campus."""
    todos_campus = find_all_campus()
    if not todos_campus:
        print(f"{cores['vermelho']}Nenhum campus encontrado.{cores['reset']}")
        return []

    campus_list = list(todos_campus)

    print("\nEscolha um campus:")
    for i, campus in enumerate(campus_list, 1):
        print(f"{i}. {campus}")

    escolha_campus = input("Escolha o número do campus: ").strip()
    while not eh_indice_valido(escolha_campus, len(campus_list)):
        print(f"{cores['vermelho']}Opção inválida! Tente novamente.{cores['reset']}")
        escolha_campus = input("Escolha o número do campus: ").strip()

    campus_index = int(escolha_campus) - 1
    campus_name = campus_list[campus_index]

    cursos = find_cursos_by_campus(campus_name)
    cursos_lista = list(cursos)
    
    if cursos_lista:
        print(f"Cursos encontrados para o campus: {campus_name}")
        exibir_lista_objeto(cursos_lista)
        return cursos_lista
    else:
        print(f"{cores['vermelho']}Nenhum curso encontrado para o campus '{campus_name}'.{cores['reset']}")
        return []

def buscar_cursos_por_tipo():
    """Busca cursos por tipo."""
    tipo_list = find_all_tipo_curso()
    if not tipo_list:
        print(f"{cores['vermelho']}Nenhum tipo de curso encontrado.{cores['reset']}")
        return []

    print("\nEscolha um tipo de curso:")
    for i, tipo in enumerate(tipo_list, 1):
        print(f"{i}. {tipo}")

    escolha_tipo = input("Escolha o número do tipo de curso: ").strip()
    while not eh_indice_valido(escolha_tipo, len(tipo_list)):
        print(f"{cores['vermelho']}Opção inválida! Tente novamente.{cores['reset']}")
        escolha_tipo = input("Escolha o número do tipo de curso: ").strip()

    tipo_index = int(escolha_tipo) - 1
    tipo_name = tipo_list[tipo_index]

    cursos = find_cursos_by_tipo(tipo_name)
    cursos_lista = list(cursos)

    if cursos_lista:
        print(f"Cursos encontrados para o tipo: {tipo_name}")
        exibir_lista_objeto(cursos_lista)
        return cursos_lista
    else:
        print(f"{cores['vermelho']}Nenhum curso encontrado para o tipo '{tipo_name}'.{cores['reset']}")
        return []

def buscar_cursos_por_nome():
    """Busca cursos por nome."""
    nome_curso = input("Digite o nome do curso: ").strip()
    while not nome_curso:
        print(f"{cores['vermelho']}Nome do curso é obrigatório.{cores['reset']}")
        nome_curso = input("Digite o nome do curso: ").strip()

    cursos = find_cursos_by_nome(nome_curso)
    cursos_lista = list(cursos)

    if cursos_lista:
        print(f"Cursos encontrados com o nome '{nome_curso}':")
        exibir_lista_objeto(cursos_lista)
        return cursos_lista
    else:
        print(f"{cores['vermelho']}Nenhum curso encontrado com o nome '{nome_curso}'.{cores['reset']}")
        return []

def atualizar_curso(id_curso):
    """Função para atualizar dados de um curso."""
    curso_encontrado = find_curso_by_id(id_curso)
    print("Detalhes atuais do curso:")
    visualizar_detalhes(curso_encontrado)
    
    novos_dados = {}
    # NOME
    nome_novo = input("Novo nome do curso (deixe em branco para manter o atual): ").strip()
    if nome_novo:
        novos_dados['nome_curso'] = nome_novo

    # CAMPUS
    campus_list = find_all_campus()
    print("\nEscolha um campus:")
    for i, campus in enumerate(campus_list, 1):
        print(f"{i}. {campus}")

    campus_novo = input("Escolha o número do campus (deixe em branco para manter o atual): ").strip()
    while not (eh_indice_valido(campus_novo, len(campus_list)) or campus_novo == ""):
        print(f"{cores['vermelho']}Opção inválida! Tente novamente.{cores['reset']}")
        campus_novo = input("Escolha o número do campus (deixe em branco para manter o atual): ").strip()
    if campus_novo:
        novos_dados['campus_curso'] = campus_list[int(campus_novo) - 1]

    # TIPO
    tipo_list = find_all_tipo_curso()
    print("\nEscolha um tipo de curso:")
    for i, tipo in enumerate(tipo_list, 1):
        print(f"{i}. {tipo}")

    tipo_novo = input("Escolha o número do tipo de curso (deixe em branco para manter o atual): ").strip()
    while not (eh_indice_valido(tipo_novo, len(tipo_list)) or tipo_novo == ""):
        print(f"{cores['vermelho']}Opção inválida! Tente novamente.{cores['reset']}")
        tipo_novo = input("Escolha o número do tipo de curso (deixe em branco para manter o atual): ").strip()
    if tipo_novo:
        novos_dados['tipo_curso'] = tipo_list[int(tipo_novo) - 1]

    # VAGAS
    vagas_novo = input("Novo número de vagas (deixe em branco para manter o atual): ").strip()
    while not ((vagas_novo.isdigit() and int(vagas_novo) >= 0) or vagas_novo == ""):
        print(f"{cores['vermelho']}Número de vagas inválido. Digite um número inteiro maior ou igual a 0.{cores['reset']}")
        vagas_novo = input("Novo número de vagas (deixe em branco para manter o atual): ").strip()
    if vagas_novo:
        novos_dados['vagas_curso'] = int(vagas_novo)

    # SEMESTRE
    todos_semestres = find_all_semestres()
    if todos_semestres:
        semestres_list = list(todos_semestres)
        if len(semestres_list) > 0:
            print("\nEscolha um semestre:")
            for i, semestre in enumerate(semestres_list, 1):
                print(f"{i}. {semestre['ano']}/{semestre['numero_semestre']}")
            
            semestre_novo = input("Escolha o número do semestre (deixe em branco para manter o atual): ").strip()
            while not (eh_indice_valido(semestre_novo, len(semestres_list)) or semestre_novo == ""):
                print(f"{cores['vermelho']}Opção inválida! Tente novamente.{cores['reset']}")
                semestre_novo = input("Escolha o número do semestre (deixe em branco para manter o atual): ").strip()
            if semestre_novo:
                novos_dados['semestre'] = semestres_list[int(semestre_novo) - 1]["_id"]
    
    # PROFESSORES
    todos_professores = find_all_professores()
    if todos_professores:
        professores = list(todos_professores)
        if len(professores) > 0:
            print("\nEscolha os professores:")
            for i, professor in enumerate(professores, 1):
                print(f"{i}. {professor['nome_professor']}")
                
            selecionados = input("Digite os números dos professores separados por vírgula (deixe em branco para manter os atuais): ").strip().split(",")
            while not (all(eh_indice_valido(selecionado, len(professores)) for selecionado in selecionados) or selecionados == ['']):
                print(f"{cores['vermelho']}Ao menos um dos números é inválido. Tente novamente.{cores['reset']}")
                selecionados = input("Digite os números dos professores separados por vírgula (deixe em branco para manter os atuais): ").strip().split(",")
            
            if selecionados != ['']:
                novos_dados['professores'] = [professores[int(selecionado) - 1]["_id"] for selecionado in selecionados]


    if novos_dados:
        atualizar_curso_no_banco(curso_encontrado, novos_dados)
        return novos_dados
    else:
        print(f"{cores['verde']}Nenhuma alteração foi feita.{cores['reset']}")
        return {}

def deletar_curso(id_curso):
    """Função para deletar um curso."""
    curso_encontrado = find_curso_by_id(id_curso)
    print(f"{cores['vermelho']}Você está prestes a excluir o curso '{curso_encontrado['nome_curso']}' do campus '{curso_encontrado['campus_curso']}'.{cores['reset']}")
    confirmar = input("Tem certeza? [S/N]: ").strip().lower()
    if len(confirmar) > 0 and confirmar[0] == 's':
        remover_curso_do_banco(curso_encontrado)
    else:
        print(f"{cores['verde']}Deleção cancelada.{cores['reset']}")
