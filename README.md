# Supermercado APIRest 🛒

Este é um projeto que visa exemplificar de forma simples um sistema de supermercado, com cadastro de itens, lojas, controle de estoque, cadastro de clientes, preenchimento de carrinho de compras e emissão de nota fiscal.

## Tecnologias utilizadas 🚀

As seguintes libs serão utilizadas para o desenvolvimento do aplicativo

- flask : Pacote que disponibiliza um servidor web para desenvolvimento e produção.
- flask-smorest : Pacote para facilitar a criação de ApiRest usando o flask.
- flask-sqlalchemy e sqlalchemy : Pacote para criar modelos Orm para interatividade com dados em um banco de dados relacional.
- flask-migrate : Usado para facilitar na atualização de schemas de banco de dados, com controle de versionamento.

Além destes pacotes Python também é disponibilizado um arquivo Dockerfile para a montagem de um container.

### Tecnologias secundarias para desenvolvimento e teste

No ambiente de desenvolvimento é usado o insomnia para criação das rotas de teste da ApiRest e validação visual do usuário.

#### Como o projeto esta organizado ?

O projeto foi organizado em estruturas de pasta que separam as responsabilidades de cada entidade no projeto. A estrutura de pastas segue a seguinte abaixo.

| NOME          | DESCRIÇÃO                                                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| resresources/ | Armazena arquivos para comunicação com as rotas (endpoint) do sistema                                                                        |
| models/       | Armazena os modelos para interatividade com o banco de dados do projeto, modelos ORM.                                                        |
| schemas/      | Os schemas tanto de validação quanto de retorno dos dados da API são disponibilizados aqui.                                                  |
| extensions.py | O arquivo é responsável por centralizar partes inicializadas e usadas sobre todo o App como o db para criação dos modelos do banco de dados. |
| app.py        | Área de inicialização do app, tem uma função que retorna uma instancia do app em Flask.                                                      |

#### 🤔 Como inicializar o aplicativo ?

Se você estiver instalando a primeira vez este sistema basta criar um **ambiente virtual** (.venv) e instalar os pacotes no _requirements.txt_.

```
python3.10 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

Então criar um arquivo .env que tenha as mesmas variaveis preenchidas do arquivo **.env_example**

Após isto basta iniciar o aplicativo (em ambiente de desenvolvimento) com:

```
./start_app.sh
```
