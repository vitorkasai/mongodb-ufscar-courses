#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from repository import *


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
        cursos = find_cursos_by_campus(campus_name)

        print("Cursos encontrados para o campus: " + campus_name)
        for curso in cursos:
            print(f"Nome do Curso: {curso['nome_curso']}")
            print(f"Campus: {curso['campus_curso']}")
            print(f"Tipo de Curso: {curso['tipo_curso']}")
            print(f"Vagas: {curso['vagas_curso']}")
            print("-" * 30)
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
        cursos = find_cursos_by_tipo(tipo_nome)

        print("Cursos encontrados para o tipo de curso: " + tipo_nome)
        for curso in cursos:
            print(f"Nome do Curso: {curso['nome_curso']}")
            print(f"Campus: {curso['campus_curso']}")
            print(f"Tipo de Curso: {curso['tipo_curso']}")
            print(f"Vagas: {curso['vagas_curso']}")
            print("-" * 30)
    except ValueError:
        print("Entrada inválida. Por favor, escolha um número válido.")


def buscar_cursos_por_nome():
    nome_curso = input("Digite o nome do curso: ")
    cursos = find_cursos_by_nome(nome_curso)

    if not cursos:
        print(f"Nenhum curso encontrado com o nome: {nome_curso}")
        return

    print(f"\nCursos encontrados com o nome '{nome_curso}':")
    for curso in cursos:
        print(f"Nome do Curso: {curso['nome_curso']}")
        print(f"Campus: {curso['campus_curso']}")
        print(f"Tipo de Curso: {curso['tipo_curso']}")
        print(f"Vagas: {curso['vagas_curso']}")
        print("-" * 30)


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
