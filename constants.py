# Definindo as cores
cores = {
    "azul": "\033[34m",
    "amarelo": "\033[33m",
    "laranja": "\033[38;5;214m",  # Laranja aproximado
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "reset": "\033[0m",  # Resetar para a cor padrão
}

tables = {
    "curso": "curso",
    "semestre": "semestre",
    "professor": "professor",
}

admin_menu_opcoes = {
    tables["curso"]: {
        "opcao": "Administrar cursos",
        "table": tables["curso"],
        "crud_opcoes": [
            "Buscar cursos por campus",
            "Buscar cursos por tipo",
            "Buscar cursos por nome",
            "Buscar cursos por semestre",
            "Buscar cursos por professor",
            "Cadastrar novo curso",
        ],
    },

    tables["semestre"]: {
        "opcao": "Administrar semestres",
        "table": tables["semestre"],
        "crud_opcoes": [
            "Buscar semestres",
            "Cadastrar novo semestre",
        ],
    },
    tables["professor"]: {
        "opcao": "Administrar professores",
        "table": tables["professor"],
        "crud_opcoes": [
            "Buscar professores",
            "Buscar professor por nome",
            "Buscar professores por curso",
            "Cadastrar novo professor",
        ],
    },
}