# Sistema de Gerenciamento de Cursos

## Descrição

Este sistema permite o gerenciamento de cursos universitários, incluindo funcionalidades para cadastro, atualização, remoção e busca de cursos por diferentes critérios, como campus, tipo e nome do curso. A aplicação se conecta a um banco de dados MongoDB para armazenar e manipular as informações dos cursos. Há ainda informações adicionais que podem ser inseridas tais como o semestre do curso e o(s) professore(s) responsável(is).
Existe ainda a possibilidade de exportar os dados de uma determinada coleção como CSV ou JSON.


## Tecnologias Utilizadas

- Python 3
- MongoDB
- Bibliotecas Python:
  - `pymongo` para interação com o MongoDB
  - `dotenv` para carregamento de variáveis de ambiente


## Como Rodar o Projeto

### Pré-requisitos

- Python 3.x instalado
- MongoDB em execução (local ou em um servidor remoto)

### Instalação

1. Clone este repositório para sua máquina local:

   ```bash
   git clone git@github.com:vitorkasai/mongodb-ufscar-courses.git
   cd mongodb-ufscar-courses
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt

4. Crie o arquivo .env com as variáveis de ambiente necessárias:

    ```bash
    MONGO_URL=mongodb://<usuario>:<senha>@<host>:<porta>/<nome_do_banco>
    NOME_DB=<nome_do_banco>
    NOME_CURSO_COLLECTION=<nome_da_colecao>
    NOME_PROFESSOR_COLLECTION=<nome_da_colecao>
    NOME_SEMESTRE_COLLECTION=<nome_da_colecao>
    ```

5. Execute o aplicativo:

    ```bash
    python main.py
    ```

## Como Usar

Após iniciar o aplicativo, você verá um menu interativo no terminal com as opções disponíveis.

