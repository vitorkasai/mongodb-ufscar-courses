#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from repository import *


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

    escolha_campus = input("Escolha o número do campus: ")

    try:
        campus_index = int(escolha_campus) - 1
        if campus_index < 0 or campus_index >= len(campus_list):
            print("Opção inválida.")
            return
        campus_name = campus_list[campus_index]
        cursos = list(find_cursos_by_campus(campus_name))

        if not cursos:
            print(f"Nenhum curso encontrado para o campus '{campus_name}'.")
            return

        print(f"Cursos encontrados para o campus: {campus_name}")
        exibir_lista_cursos(cursos)
        selecionar_acao(cursos)

    except ValueError:
        print("Entrada inválida. Por favor, escolha um número válido.")


def buscar_cursos_por_tipo():
    tipo_list = find_all_tipo_curso()
    if not tipo_list:
        print("Nenhum tipo de curso encontrado.")
        return

    print("\nEscolha um tipo de curso:")
    for i, tipo in enumerate(tipo_list, 1):
        print(f"{i}. {tipo}")

    escolha_tipo = input("Escolha o número do tipo de curso: ")

    try:
        tipo_index = int(escolha_tipo) - 1
        if tipo_index < 0 or tipo_index >= len(tipo_list):
            print("Opção inválida.")
            return
        tipo_nome = tipo_list[tipo_index]
        cursos = list(find_cursos_by_tipo(tipo_nome))

        if not cursos:
            print(f"Nenhum curso encontrado para o tipo '{tipo_nome}'.")
            return

        print(f"Cursos encontrados para o tipo de curso: {tipo_nome}")
        exibir_lista_cursos(cursos)
        selecionar_acao(cursos)

    except ValueError:
        print("Entrada inválida. Por favor, escolha um número válido.")


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
    try:
        escolha = int(input("Escolha o número do curso para atualizar ou remover (0 para voltar): "))
        if escolha == 0:
            return

        if escolha < 1 or escolha > len(cursos):
            print("Opção inválida. Tente novamente.")
            return

        curso_selecionado = cursos[escolha - 1]
        acao = input(f"Você escolheu o curso '{curso_selecionado['nome_curso']}'. Deseja (a)tualizar ou (r)emover? ")

        if acao.lower() == 'a':
            atualizar_curso(curso_selecionado)
        elif acao.lower() == 'r':
            remover_curso(curso_selecionado)
        else:
            print("Opção inválida. Por favor, escolha 'a' para atualizar ou 'r' para remover.")

    except ValueError:
        print("Entrada inválida. Por favor, escolha um número válido.")


def atualizar_curso(curso):
    print(f"Atualizando o curso: {curso['nome_curso']}")
    nome_curso = input(f"Novo nome do curso (atualmente: {curso['nome_curso']}, deixe em branco para não alterar): ")

    campus_list = find_all_campus()
    if not campus_list:
        print("Nenhum campus encontrado.")
        return

    print("\nEscolha um campus (deixe em branco para não alterar):")
    for i, campus in enumerate(campus_list, 1):
        print(f"{i}. {campus}")

    campus_atual = curso['campus_curso']
    escolha_campus = input(f"Campus atual: {campus_atual}\nEscolha o número do campus ou pressione Enter para manter: ")

    if escolha_campus:
        try:
            campus_index = int(escolha_campus) - 1
            if campus_index < 0 or campus_index >= len(campus_list):
                print("Opção inválida.")
                return
            campus_nome = campus_list[campus_index]
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")
            return
    else:
        campus_nome = campus_atual

    tipo_list = find_all_tipo_curso()
    if not tipo_list:
        print("Nenhum tipo de curso encontrado.")
        return

    print("\nEscolha um tipo de curso (deixe em branco para não alterar):")
    for i, tipo in enumerate(tipo_list, 1):
        print(f"{i}. {tipo}")

    tipo_atual = curso['tipo_curso']
    escolha_tipo = input(f"Tipo de curso atual: {tipo_atual}\nEscolha o número do tipo ou pressione Enter para manter: ")

    if escolha_tipo:
        try:
            tipo_index = int(escolha_tipo) - 1
            if tipo_index < 0 or tipo_index >= len(tipo_list):
                print("Opção inválida.")
                return
            tipo_nome = tipo_list[tipo_index]
        except ValueError:
            print("Entrada inválida. Por favor, escolha um número válido.")
            return
    else:
        tipo_nome = tipo_atual

    vagas_curso = input(f"Número de vagas atual: {curso['vagas_curso']}\nNovo número de vagas (deixe em branco para não alterar): ")

    try:
        if vagas_curso:
            vagas_curso = int(vagas_curso)
        else:
            vagas_curso = curso['vagas_curso']
    except ValueError:
        print("Número de vagas inválido.")
        return

    novos_dados = {
        "nome_curso": nome_curso or curso['nome_curso'],
        "campus_curso": campus_nome,
        "tipo_curso": tipo_nome,
        "vagas_curso": vagas_curso
    }

    atualizar_curso_no_banco(curso, novos_dados)


def remover_curso(curso):
    confirmar = input(f"Você tem certeza que deseja remover o curso '{curso['nome_curso']}'? (s/n): ")
    if confirmar.lower() == 's':
        remover_curso_do_banco(curso)


def cadastrar_novo_curso():
    print("\n--- Cadastro de Novo Curso ---")

    nome_curso = input("Nome do Curso: ")

    campus_list = find_all_campus()
    if not campus_list:
        print("Nenhum campus encontrado.")
        return

    print("\nEscolha um campus:")
    for i, campus in enumerate(campus_list, 1):
        print(f"{i}. {campus}")
    escolha_campus = input("Escolha o número do campus: ")

    try:
        campus_index = int(escolha_campus) - 1
        if campus_index < 0 or campus_index >= len(campus_list):
            print("Opção inválida.")
            return
        campus_nome = campus_list[campus_index]
    except ValueError:
        print("Entrada inválida. Por favor, escolha um número válido.")
        return

    tipo_list = find_all_tipo_curso()
    if not tipo_list:
        print("Nenhum tipo de curso encontrado.")
        return

    print("\nEscolha um tipo de curso:")
    for i, tipo in enumerate(tipo_list, 1):
        print(f"{i}. {tipo}")
    escolha_tipo = input("Escolha o número do tipo de curso: ")

    try:
        tipo_index = int(escolha_tipo) - 1
        if tipo_index < 0 or tipo_index >= len(tipo_list):
            print("Opção inválida.")
            return
        tipo_nome = tipo_list[tipo_index]
    except ValueError:
        print("Entrada inválida. Por favor, escolha um número válido.")
        return

    vagas_curso = input("Número de Vagas: ")

    try:
        vagas_curso = int(vagas_curso)
    except ValueError:
        print("Número de vagas inválido. Deve ser um número inteiro.")
        return

    curso = {
        "nome_curso": nome_curso,
        "campus_curso": campus_nome,
        "tipo_curso": tipo_nome,
        "vagas_curso": vagas_curso
    }

    inserir_novo_curso(curso)
    print(f"\nCurso '{nome_curso}' cadastrado com sucesso!")
