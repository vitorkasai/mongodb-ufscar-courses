from . import get_db_connection, getenv

# Funções para trabalhar com cursos
def inserir_novo_curso(curso):
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    resultado = collection.insert_one(curso)
    return resultado

def find_all_cursos():
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    return collection.find()

def find_cursos_by_campus(campus_curso):
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    cursos_encontrados = collection.find({"campus_curso": campus_curso})
    return cursos_encontrados

def find_cursos_by_tipo(tipo_curso):
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    cursos_encontrados = collection.find({"tipo_curso": tipo_curso})
    return cursos_encontrados

def find_curso_by_id(curso_id):
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    curso = collection.find_one({"_id": curso_id})
    return curso

def find_curso_by_semestre(id_semestre):
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    cursos_encontrados = collection.find({"semestre": id_semestre})
    return cursos_encontrados

def find_cursos_by_professor(id_professor):
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    cursos_encontrados = collection.find({"professor": id_professor})
    return cursos_encontrados

def find_cursos_by_nome(nome_curso):
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    cursos_encontrados = collection.find({"nome_curso": {"$regex": nome_curso, "$options": "i"}})
    return cursos_encontrados

def find_all_campus():
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    campus_list = collection.distinct("campus_curso")
    return campus_list

def find_all_tipo_curso():
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    tipo_list = collection.distinct("tipo_curso")
    return tipo_list

def atualizar_curso_no_banco(curso, novos_dados):
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    resultado = collection.update_one(
        {"nome_curso": curso['nome_curso'], "campus_curso": curso['campus_curso']},
        {"$set": novos_dados}
    )
    if resultado.matched_count:
        print("Curso atualizado com sucesso.")
    else:
        print("Curso não encontrado.")

def remover_curso_do_banco(curso):
    collection = get_db_connection(getenv("NOME_CURSO_COLLECTION"))
    resultado = collection.delete_one({"nome_curso": curso['nome_curso'], "campus_curso": curso['campus_curso']})
    if resultado.deleted_count:
        print("Curso removido com sucesso.")
        return True
    else:
        print("Curso não encontrado.")
        return False
    