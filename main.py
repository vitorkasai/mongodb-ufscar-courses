#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import encerrar_programa, exibir_menu, admin_menu_opcoes, executar_crud, cores, tables, export_data
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
            if escolha.isdigit() and int(escolha) in [4, 5]:
                formato = "csv" if int(escolha) == 4 else "json"
                print(f"Tabelas disponíveis para exportar em {formato.upper()}:")
                for indice, nome_tabela in enumerate(tables.values(), 1):
                    print(f"{indice}. {nome_tabela.capitalize()}")
                escolha_tabela = input("Escolha uma opção (deixe vazio para voltar): ").strip().lower()
                while not (eh_indice_valido(escolha_tabela, len(tables)) or escolha_tabela == ""):
                    print(f"{cores['vermelho']}Opção inválida. Por favor, escolha uma opção válida.{cores['reset']}")
                    escolha_tabela = input("Escolha uma opção (deixe vazio para voltar): ").strip().lower()
                if escolha_tabela != "":
                    indice = int(escolha_tabela) - 1
                    tabela_escolhida = list(tables.values())[indice]
                    print(f"{cores['verde']}\nExportando dados da tabela {tabela_escolhida.capitalize()} para {formato.upper()}...{cores['reset']}")
                    if formato == 'csv':
                        export_data(tabela_escolhida, 'csv')
                    else:
                        export_data(tabela_escolhida, 'json')
            else:
                print(f"{cores['vermelho']}Opção inválida. Por favor, escolha uma opção válida.{cores['reset']}")

if __name__ == "__main__":
    main()
