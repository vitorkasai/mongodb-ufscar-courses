from . import get_db_connection, getenv

# Funções para trabalhar com semestres
def inserir_novo_semestre(semestre):
    collection = get_db_connection(getenv("NOME_SEMESTRE_COLLECTION"))
    resultado = collection.insert_one(semestre)
    return resultado

def find_all_semestres():
    collection = get_db_connection(getenv("NOME_SEMESTRE_COLLECTION"))
    return collection.find()

def find_semestre_by_id(semestre_id):
    collection = get_db_connection(getenv("NOME_SEMESTRE_COLLECTION"))
    semestre = collection.find_one({"_id": semestre_id})
    return semestre

def find_semestre_by_status(status):
    collection = get_db_connection(getenv("NOME_SEMESTRE_COLLECTION"))
    return collection.find({"status": status})

def atualizar_semestre_no_banco(semestre_id, novos_dados):
    collection = get_db_connection(getenv("NOME_SEMESTRE_COLLECTION"))
    resultado = collection.update_one(
        {"_id": semestre_id},
        {"$set": novos_dados}
    )
    if resultado.matched_count:
        print("Semestre atualizado com sucesso.")
    else:
        print("Semestre não encontrado.")

def remover_semestre_do_banco(semestre_id):
    collection = get_db_connection(getenv("NOME_SEMESTRE_COLLECTION"))
    resultado = collection.delete_one({"_id": semestre_id})
    if resultado.deleted_count > 0:
        print("Semestre removido com sucesso.")
    else:
        print("Semestre não encontrado.")