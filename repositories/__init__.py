#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient, ASCENDING
from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)

def get_db_connection(collection_name):
    """Estabelece uma conexão com o banco de dados e retorna a coleção solicitada."""
    client = MongoClient(getenv("MONGO_URL"))
    db = client[getenv("NOME_DB")]
    collection = db[collection_name]
    return collection