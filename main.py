#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import *


def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção [1] | [2] | [3] | [4] | [5]: ").strip().lower()[0]
        escolha_valida = eh_indice_valido(escolha, len(admin_menu_opcoes))
        if escolha_valida:
            admin_menu_opcoes[int(escolha) - 1]["handler"]()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
