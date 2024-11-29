#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from repository import *
from helpers import eh_indice_valido



def exibir_lista_cursos(cursos):
    for i, curso in enumerate(cursos, 1):
        print(f"{i}. {curso['nome_curso']} - {curso['campus_curso']} - {curso['tipo_curso']} - {curso['vagas_curso']} vagas")
    print("-" * 30)


def buscar_cursos_por_campus():
    campus_list = find_all_campus()
    if not campus_list:
        print("Nenhum campus encontrado.")
        return

    print("\nEscolha um campus:")
    for i, campus in enumerate(campus_list, 1):
        print(f"{i}. {campus}")

    escolha_campus = input("Escolha o número do campus: ").strip().lower()
    while not eh_indice_valido(escolha_campus, len(campus_list)):
        print("Opção inválida. Tente novamente.")
        escolha_campus = input("Escolha o número do campus: ").strip().lower()

    campus_index = int(escolha_campus) - 1
    campus_name = campus_list[campus_index]
    cursos = list(find_cursos_by_campus(campus_name))

    if not cursos:
        print(f"Nenhum curso encontrado para o campus '{campus_name}'.")
        return

    print(f"Cursos encontrados para o campus: {campus_name}")
    exibir_lista_cursos(cursos)
    selecionar_acao(cursos)


def buscar_cursos_por_tipo():
    tipo_list = find_all_tipo_curso()
    if not tipo_list:
        print("Nenhum tipo de curso encontrado.")
        return

    print("\nEscolha um tipo de curso:")
    for i, tipo in enumerate(tipo_list, 1):
        print(f"{i}. {tipo}")

    escolha_tipo = input("Escolha o número do tipo de curso: ").strip().lower()
    while not eh_indice_valido(escolha_tipo, len(tipo_list)):
        print("Opção inválida. Tente novamente.")
        escolha_tipo = input("Escolha o número do tipo de curso: ").strip().lower()
       
    tipo_index = int(escolha_tipo) - 1
    tipo_nome = tipo_list[tipo_index]
    cursos = list(find_cursos_by_tipo(tipo_nome))

    if not cursos:
        print(f"Nenhum curso encontrado para o tipo '{tipo_nome}'.")
        return

    print(f"Cursos encontrados para o tipo de curso: {tipo_nome}")
    exibir_lista_cursos(cursos)
    selecionar_acao(cursos)


def buscar_cursos_por_nome():
    nome_curso = input("Digite o nome do curso: ")
    cursos = list(find_cursos_by_nome(nome_curso))

    if not cursos:
        print(f"Nenhum curso encontrado com o nome: {nome_curso}")
        return

    print(f"\nCursos encontrados com o nome '{nome_curso}':")
    exibir_lista_cursos(cursos)
    selecionar_acao(cursos)


def selecionar_acao(cursos):
    escolha = input("Escolha o número do curso para atualizar ou remover (0 para voltar): ").strip().lower()
    while not eh_indice_valido(escolha, len(cursos), 0):
        print("Opção inválida. Tente novamente.")
        escolha = input("Escolha o número do curso para atualizar ou remover (0 para voltar): ").strip().lower()

    if int(escolha) == 0:
        return

    curso_selecionado = cursos[int(escolha) - 1]
    acao = input(f"Você escolheu o curso '{curso_selecionado['nome_curso']}'. Deseja (a)tualizar ou (r)emover? (deixe vazio para voltar) ").strip().lower()
    while not (acao == '' or  acao[0] in ['a', 'r']):
        print("Opção inválida. Por favor, escolha 'a' para atualizar ou 'r' para remover.")
        acao = input(f"Você escolheu o curso '{curso_selecionado['nome_curso']}'. Deseja (a)tualizar ou (r)emover? (deixe vazio para voltar) ").strip().lower()

    if acao and acao[0] == 'a':
        atualizar_curso(curso_selecionado)
    elif acao and acao[0] == 'r':
        remover_curso(curso_selecionado)



def atualizar_curso(curso):
    print(f"Atualizando o curso: {curso['nome_curso']}")
    nome_curso = input(f"Novo nome do curso (atualmente: \"{curso['nome_curso']}\", ou deixe em branco para não alterar): ").strip()

    campus_list = find_all_campus()
    if not campus_list:
        print("Nenhum campus encontrado.")
        return

    print("\nEscolha um campus (deixe em branco para não alterar):")
    for i, campus in enumerate(campus_list, 1):
        print(f"{i}. {campus}")

    campus_atual = curso['campus_curso']
    escolha_campus = input(f"Campus atual: {campus_atual}\nEscolha o número do campus ou pressione Enter para manter: ").strip().lower()
    while not (eh_indice_valido(escolha_campus, len(campus_list)) or escolha_campus == ""):
        print("Opção inválida. Tente novamente.")
        escolha_campus = input(f"Campus atual: {campus_atual}\nEscolha o número do campus ou pressione Enter para manter: ").strip().lower()

    campus_nome = campus_atual
    if escolha_campus:
        campus_index = int(escolha_campus) - 1
        campus_nome = campus_list[campus_index]

    tipo_list = find_all_tipo_curso()
    if not tipo_list:
        print("Nenhum tipo de curso encontrado.")
        return

    print("\nEscolha um tipo de curso (deixe em branco para não alterar):")
    for i, tipo in enumerate(tipo_list, 1):
        print(f"{i}. {tipo}")

    tipo_atual = curso['tipo_curso']
    escolha_tipo = input(f"Tipo de curso atual: {tipo_atual}\nEscolha o número do tipo ou pressione Enter para manter: ").strip().lower()
    while not (eh_indice_valido(escolha_tipo, len(tipo_list)) or escolha_tipo == ""):
        print("Opção inválida. Tente novamente.")
        escolha_tipo = input(f"Tipo de curso atual: {tipo_atual}\nEscolha o número do tipo ou pressione Enter para manter: ").strip().lower()

    tipo_nome = tipo_atual
    if escolha_tipo:
        tipo_index = int(escolha_tipo) - 1
        tipo_nome = tipo_list[tipo_index]

    vagas_curso = input(f"Número de vagas atual: {curso['vagas_curso']}\nNovo número de vagas (deixe em branco para não alterar): ").strip().lower()
    while not ((vagas_curso.isdigit() and int(vagas_curso) >= 0) or vagas_curso == ""):
        print("Número de vagas inválido. Tente novamente.")
        vagas_curso = input(f"Número de vagas atual: {curso['vagas_curso']}\nNovo número de vagas (deixe em branco para não alterar): ").strip().lower()

    if vagas_curso != "":
        vagas_curso = int(vagas_curso)
    else:
        vagas_curso = curso['vagas_curso']
  
    novos_dados = {
        "nome_curso": nome_curso or curso['nome_curso'],
        "campus_curso": campus_nome,
        "tipo_curso": tipo_nome,
        "vagas_curso": vagas_curso
    }

    atualizar_curso_no_banco(curso, novos_dados)


def remover_curso(curso):
    confirmar = input(f"Você tem certeza que deseja remover o curso '{curso['nome_curso']}'? (s/n): ").strip().lower()
    while not confirmar in ['s', 'n']:
        print("Opção inválida. Por favor, escolha 's' para confirmar ou 'n' para cancelar.")
        confirmar = input(f"Você tem certeza que deseja remover o curso '{curso['nome_curso']}'? (s/n): ").strip().lower()
    if confirmar == 's':
        remover_curso_do_banco(curso)


def cadastrar_novo_curso():
    print("\n--- Cadastro de Novo Curso ---")

    nome_curso = input("Nome do Curso: ").strip()

    campus_list = find_all_campus()
    if not campus_list:
        print("Nenhum campus encontrado.")
        return

    print("\nEscolha um campus:")
    for i, campus in enumerate(campus_list, 1):
        print(f"{i}. {campus}")
    escolha_campus = input("Escolha o número do campus: ").strip().lower()
    while not eh_indice_valido(escolha_campus, len(campus_list)):
        print("Opção inválida. Tente novamente.")
        escolha_campus = input("Escolha o número do campus: ").strip().lower()

    campus_index = int(escolha_campus) - 1
    campus_nome = campus_list[campus_index]

    tipo_list = find_all_tipo_curso()
    if not tipo_list:
        print("Nenhum tipo de curso encontrado.")
        return

    print("\nEscolha um tipo de curso:")
    for i, tipo in enumerate(tipo_list, 1):
        print(f"{i}. {tipo}")

    escolha_tipo = input("Escolha o número do tipo de curso: ").strip().lower()
    while not eh_indice_valido(escolha_tipo, len(tipo_list)):
        print("Opção inválida. Tente novamente.")
        escolha_tipo = input("Escolha o número do tipo de curso: ").strip().lower()

    tipo_index = int(escolha_tipo) - 1
    tipo_nome = tipo_list[tipo_index]

    vagas_curso = input("Número de Vagas: ").strip().lower()
    while not (vagas_curso.isdigit() and int(vagas_curso) >= 0):
        print("Número de vagas inválido. Tente novamente.")
        vagas_curso = input("Número de Vagas: ").strip().lower()

    vagas_curso = int(vagas_curso)

    curso = {
        "nome_curso": nome_curso,
        "campus_curso": campus_nome,
        "tipo_curso": tipo_nome,
        "vagas_curso": vagas_curso
    }

    inserir_novo_curso(curso)
    print(f"\nCurso '{nome_curso}' cadastrado com sucesso!")
