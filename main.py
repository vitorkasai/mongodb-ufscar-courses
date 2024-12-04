#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import encerrar_programa, exibir_menu, admin_menu_opcoes, executar_crud, cores
from helpers import eh_indice_valido

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip().lower()
        if escolha == "0":
            encerrar_programa()

        escolha_valida = eh_indice_valido(escolha, len(admin_menu_opcoes))
        
        if escolha_valida:
            indice = int(escolha) - 1
            tabela_escolhida = list(admin_menu_opcoes.keys())[indice]
            print(f"{cores['verde']}\nMenu acessado: {admin_menu_opcoes[tabela_escolhida]['opcao']}{cores['reset']}")
            executar_crud(tabela_escolhida)
        else:
            print(f"{cores['vermelho']}Opção inválida. Por favor, escolha uma opção válida.{cores['reset']}")

if __name__ == "__main__":
    main()
