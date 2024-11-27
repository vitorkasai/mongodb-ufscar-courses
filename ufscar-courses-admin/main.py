#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from services import *


def exibir_menu():
    print("\n--- Menu ---")
    print("1. Buscar cursos por campus")
    print("2. Buscar cursos por tipo de curso")
    print("3. Buscar cursos por nome")
    print("4. Cadastrar novo curso")
    print("5. Sair")
    escolha = input("Escolha uma opção (1/2/3/4/5): ")
    return escolha


def main():
    while True:
        escolha = exibir_menu()

        if escolha == "1":
            buscar_cursos_por_campus()
        elif escolha == "2":
            buscar_cursos_por_tipo()
        elif escolha == "3":
            buscar_cursos_por_nome()
        elif escolha == "4":
            cadastrar_novo_curso()
        elif escolha == "5":
            print("Finalizando programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
