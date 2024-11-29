# Sistema de Gerenciamento de Cursos

## Descrição

Este sistema permite o gerenciamento de cursos universitários, incluindo funcionalidades para cadastro, atualização, remoção e busca de cursos por diferentes critérios, como campus, tipo e nome do curso. A aplicação se conecta a um banco de dados MongoDB para armazenar e manipular as informações dos cursos.

## Funcionalidades

- **Cadastro de Novo Curso**: Permite cadastrar um novo curso, associando-o a um campus e tipo de curso, além de definir o número de vagas.
- **Busca de Cursos**:
  - Buscar por campus
  - Buscar por tipo de curso
  - Buscar por nome de curso
- **Atualização de Curso**: Permite atualizar o nome, campus, tipo e número de vagas de um curso existente.
- **Remoção de Curso**: Permite remover um curso do sistema.

## Tecnologias Utilizadas

- Python 3
- MongoDB
- Bibliotecas Python:
  - `pymongo` para interação com o MongoDB
  - `dotenv` para carregamento de variáveis de ambiente

## Estrutura de Diretórios

```bash
.
├── repository.py       # Funções para interagir com o banco de dados
├── services.py         # Lógica de negócios e manipulação dos cursos
├── utils.py            # Funções utilitárias
├── helpers.py          # Funções auxiliares
├── main.py             # Arquivo principal que executa a aplicação
├── .env                # Arquivo de configuração de variáveis de ambiente
└── README.md           # Este arquivo
```

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
    NOME_COLLECTION=<nome_da_colecao>
    ```

5. Execute o aplicativo:

    ```bash
    python main.py
    ```

## Como Usar

Após iniciar o aplicativo, você verá um menu interativo no terminal com as seguintes opções:

1. **Cadastrar Novo Curso**: Para cadastrar um novo curso.
2. **Buscar Cursos por Campus**: Para buscar cursos filtrados por campus.
3. **Buscar Cursos por Tipo**: Para buscar cursos filtrados por tipo.
4. **Buscar Cursos por Nome**: Para buscar cursos filtrados por nome.
5. **Sair**: Para encerrar a aplicação.

O sistema exibirá uma lista de cursos e permitirá que você escolha qual ação deseja executar (atualizar, remover ou voltar).

