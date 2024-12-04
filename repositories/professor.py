from . import get_db_connection, getenv
from constants import cores

# Funções para trabalhar com professores
def inserir_novo_professor(professor):
    collection = get_db_connection(getenv("NOME_PROFESSOR_COLLECTION"))
    resultado = collection.insert_one(professor)
    return resultado

def find_professor_by_id(professor_id):
    collection = get_db_connection(getenv("NOME_PROFESSOR_COLLECTION"))
    professor = collection.find_one({"_id": professor_id})
    return professor

def find_all_professores():
    collection = get_db_connection(getenv("NOME_PROFESSOR_COLLECTION"))
    return collection.find()

def find_professores_by_curso(curso_id):
    collection = get_db_connection(getenv("NOME_PROFESSOR_COLLECTION"))
    return collection.find({"cursos": {"$in": [curso_id]}})

def find_professor_by_nome(nome_professor):
    collection = get_db_connection(getenv("NOME_PROFESSOR_COLLECTION"))
    professor = collection.find_one({"nome_professor": {"$regex": nome_professor, "$options": "i"}})
    return professor

def atualizar_professor_no_banco(professor_id, novos_dados):
    collection = get_db_connection(getenv("NOME_PROFESSOR_COLLECTION"))
    resultado = collection.update_one(
        {"_id": professor_id},
        {"$set": novos_dados}
    )
    if resultado.matched_count:
        print(f"{cores['verde']}Professor atualizado com sucesso.{cores['reset']}")
    else:
        print(f"{cores['vermelho']}Professor não encontrado.{cores['reset']}")

def remover_professor_do_banco(professor_id):
    collection = get_db_connection(getenv("NOME_PROFESSOR_COLLECTION"))
    resultado = collection.delete_one({"_id": professor_id})
    if resultado.deleted_count:
        print(f"{cores['verde']}Professor removido com sucesso.{cores['reset']}")
    else:
        print(f"{cores['vermelho']}Professor não encontrado.{cores['reset']}")