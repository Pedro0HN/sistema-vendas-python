CRUD de Vendas em Python com MySQL

Projeto simples de CRUD (Create, Read, Update, Delete) desenvolvido em Python com integração ao banco de dados MySQL.  
O objetivo do projeto é praticar operações de banco de dados, organização de código em arquivos separados e interação com o usuário via terminal.

## Funcionalidades

- Inserir vendas
- Listar vendas
- Atualizar vendas
- Deletar vendas
- Menu interativo no terminal


## Tecnologias utilizadas

- Python  
- MySQL  
- mysql-connector-python

## Estrutura do projeto

main.py - Menu interativo

database.py - Conexão com o banco de dados

crud.py - Funções CRUD

## Configuração do banco de dados

CREATE DATABASE banco_python;

Crie a Tabela:
CREATE TABLE vendas (
    idVendas INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(100),
    valor DECIMAL(10,2)

Instalação:
pip install mysql-connector-python

# Executar Projeto

python main.py

## Aprendizados

Neste projeto foram praticados:

Conexão do Python com MySQL

Operações CRUD

Organização de código em múltiplos arquivos

Uso de parâmetros SQL (prevenção de SQL Injection)

Estrutura de menu interativo no terminal
