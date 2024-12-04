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