#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from repository import find_cursos_by_campus, find_all_campus


def exibir_menu():
    print("\n--- Menu ---")
    print("1. Buscar cursos por campus")
    print("2. Sair")
    escolha = input("Escolha uma opção (1/2): ")
    return escolha


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
            print(f"Tipo de Curso: {curso['tipo_curso']}")
            print(f"Vagas: {curso['vagas_curso']}")
            print("-" * 30)
    except ValueError:
        print("Entrada inválida. Por favor, escolha um número válido.")


def main():
    while True:
        escolha = exibir_menu()

        if escolha == "1":
            buscar_cursos_por_campus()
        elif escolha == "2":
            print("Finalizando programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
