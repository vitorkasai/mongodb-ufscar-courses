#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017/"
NOME_DB = "db_admin_ufscar_courses"
NOME_COLLECTION = "tb_courses"


def get_db_connection():
    client = MongoClient(MONGO_URL)
    db = client[NOME_DB]
    collection = db[NOME_COLLECTION]
    return collection


def find_all_cursos():
    collection = get_db_connection()
    return collection.find({"_id": 0})


def find_cursos_by_campus(campus_curso):
    collection = get_db_connection()
    cursos_encontrados = collection.find({"campus_curso": campus_curso}, {"_id": 0})
    return cursos_encontrados


def find_cursos_by_tipo(tipo_curso):
    collection = get_db_connection()
    cursos_encontrados = collection.find({"tipo_curso": tipo_curso}, {"_id": 0})
    return cursos_encontrados


def find_cursos_by_nome(nome_curso):
    collection = get_db_connection()
    cursos_encontrados = collection.find({"nome_curso": {"$regex": nome_curso, "$options": "i"}}, {"_id": 0})
    return cursos_encontrados


def find_all_campus():
    collection = get_db_connection()
    campus_list = collection.distinct("campus_curso")
    return campus_list


def find_all_tipo_curso():
    collection = get_db_connection()
    tipo_list = collection.distinct("tipo_curso")
    return tipo_list


def atualizar_curso_no_banco(curso, novos_dados):
    collection = get_db_connection()
    resultado = collection.update_one(
        {"nome_curso": curso['nome_curso'], "campus_curso": curso['campus_curso']},
        {"$set": novos_dados}
    )
    if resultado.matched_count:
        print("Curso atualizado com sucesso.")
    else:
        print("Curso não encontrado.")


def remover_curso_do_banco(curso):
    collection = get_db_connection()
    resultado = collection.delete_one({"nome_curso": curso['nome_curso'], "campus_curso": curso['campus_curso']})
    if resultado.deleted_count:
        print("Curso removido com sucesso.")
    else:
        print("Curso não encontrado.")


def inserir_novo_curso(curso):
    collection = get_db_connection()
    resultado = collection.insert_one(curso)
    return resultado
