# utils.py

from services import *
from constants import admin_menu_opcoes, tables, cores
from repositories import get_db_connection
import json
import os
import csv

from services.curso import exibir_menu_curso
from services.semestre import exibir_menu_semestre
from services.professor import exibir_menu_professor

# Funções
def encerrar_programa() -> None:
    print(f"{cores['vermelho']}Finalizando programa...{cores['reset']}")
    exit()

def exibir_menu() -> None:
    print(f"{cores['azul']}\n--- Menu principal ---{cores['reset']}")
    indice = 1
    for key, value in admin_menu_opcoes.items():
        print(f"{indice}. {value['opcao']}")
        indice += 1
    # Adicionando opções a mais para download csv/json
    print(f"{indice}. Exportar dados para CSV")
    print(f"{indice + 1}. Exportar dados para JSON")
    print(f"{cores['vermelho']}0. Encerrar programa{cores['reset']}")



def executar_crud(table):
    """Função para executar o CRUD baseado na tabela."""
    if table == tables["curso"]:
        exibir_menu_curso()
    elif table == tables["semestre"]:
        exibir_menu_semestre()
    elif table == tables["professor"]:
        exibir_menu_professor()
    else:
        print(f"{cores['vermelho']}Tabela não reconhecida.{cores['reset']}")


def ensure_directory_exists(path):
    """Cria o diretório de destino, se ele não existir."""
    if not os.path.exists(path):
        os.makedirs(path)

def export_to_csv(collection, file_name):
    """Exporta os dados da coleção para um arquivo CSV, considerando todos os campos."""
    cursor = collection.find()
    all_fieldnames = set()  # Usar um set para garantir que as chaves sejam únicas

    # Itera sobre todos os documentos e coleta todas as chaves
    for document in cursor:
        all_fieldnames.update(document.keys())

    # Voltar ao início da consulta para reescrever os dados no CSV
    cursor = collection.find()

     # Definindo o caminho do diretório
    export_dir = './exported_data/csv'
    ensure_directory_exists(export_dir)
    
    # Definindo o caminho completo para o arquivo CSV
    file_path = os.path.join(export_dir, f"{file_name}")

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=all_fieldnames)
        writer.writeheader()
        for document in cursor:
            writer.writerow(document)

def export_to_json(collection, file_name):
    """Exporta os dados da coleção para um arquivo JSON, lidando com ObjectId."""
    cursor = collection.find()
    documents = list(cursor)

    # Função para converter ObjectId para string
    def convert_objectid(document):
        for key, value in document.items():
            if isinstance(value, ObjectId):
                document[key] = str(value)  # Converte ObjectId para string
        return document

    # Converte cada documento para garantir que ObjectId seja serializado corretamente
    documents = [convert_objectid(doc) for doc in documents]

     # Definindo o caminho do diretório
    export_dir = './exported_data/json'
    ensure_directory_exists(export_dir)
    
    # Definindo o caminho completo para o arquivo JSON
    file_path = os.path.join(export_dir, f"{file_name}")

    # Salvando os documentos no arquivo JSON
    with open(file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(documents, jsonfile, indent=4, ensure_ascii=False)

def export_data(collection_name, export_format):
    """Exporta os dados da coleção escolhida para o formato desejado."""
    collection = get_db_connection(collection_name)

    if export_format == 'csv':
        file_name = f"{collection_name}.csv"
        export_to_csv(collection, file_name)
        print(f"{cores['verde']}Dados exportados para {file_name}{cores['reset']}")
    elif export_format == 'json':
        file_name = f"{collection_name}.json"
        export_to_json(collection, file_name)
        print(f"{cores['verde']}Dados exportados para {file_name}{cores['reset']}")