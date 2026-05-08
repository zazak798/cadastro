# Sistema de Cadastro de Produtos (Padaria)

Este repositório contém um sistema de cadastro de itens desenvolvido em **Python**, utilizando a biblioteca **PySide6** para a interface gráfica e **MySQL** como banco de dados, rodando em ambiente **Docker**.

## 🚀 Tecnologias Utilizadas

*   **Linguagem:** Python 3.12+
*   **GUI:** PySide6 (Qt for Python)
*   **Banco de Dados:** MySQL 8.0
*   **Containerização:** Docker e Docker Compose
*   **Versionamento:** Git

## 📂 Estrutura do Projeto

*   `main.py`: Ponto de entrada da aplicação e lógica da interface.
*   `db.py`: Configuração da conexão e operações com o banco de dados MySQL.
*   `docker-compose.yml`: Configuração do ambiente para subir o serviço do banco de dados.
*   `variables.py` / `styles.py`: Definições de caminhos, cores e estilos da interface.

## ⚙️ Como Executar

### 1. Requisitos
*   Docker e Docker Compose instalados.
*   Python 3.x instalado localmente.

### 2. Configurando o Banco de Dados
Na raiz do projeto, execute o comando abaixo para iniciar o container do MySQL:
```bash
docker-compose up -d