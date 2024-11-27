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
