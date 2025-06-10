# Projeto Lista de Afazeres

## ALUNOS:
* Fillipe Ribeiro Berssot Mori
* Thiago Gabriel Dionísio da Silva

## Link Vídeo Youtube:
* https://www.youtube.com/watch?v=dIbJcWE-H10&ab_channel=Tchillz

## 🎯 Descrição

Um programa de console simples, desenvolvido em Python, para gerenciar uma lista de tarefas pessoais. Permite ao usuário adicionar, listar, atualizar e deletar tarefas, que são armazenadas localmente em um arquivo de texto.

## 🌟 Funcionalidades Principais

* **Adicionar Tarefas:** Permite ao usuário inserir novas tarefas na lista.
* **Listar Tarefas:** Exibe todas as tarefas cadastradas, numeradas para fácil visualização.
* **Atualizar Tarefas:** Permite modificar a descrição de uma tarefa existente, selecionando-a pela sua numeração.
* **Deletar Tarefas:** Remove uma tarefa da lista, também selecionando-a pela numeração e solicitando confirmação.
* **Encerrar Programa:** Finaliza a execução da aplicação.
* **Persistência de Dados:** As tarefas são salvas no arquivo `tarefas.txt` para que não sejam perdidas ao fechar o programa.

## 💻 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Módulos Python:**
    * `json`: Utilizado para serializar e desserializar as tarefas ao salvá-las e carregá-las do arquivo `tarefas.txt`.
* **Armazenamento:** Arquivo de texto (`tarefas.txt`) onde cada linha representa uma tarefa em formato JSON string.

## 🚀 Como Rodar o Projeto

### Pré-requisitos

* É necessário ter o Python 3 instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

### Instalação

1.  Clone este repositório (ou baixe os arquivos `main.py` e `funcoes.py` para uma mesma pasta no seu computador).
2.  Nenhuma instalação de biblioteca externa é necessária, pois o projeto utiliza apenas módulos padrão do Python.

### Execução

1.  Abra um terminal ou prompt de comando.
2.  Navegue até a pasta onde você salvou os arquivos do projeto.
3.  Execute o comando:
    ```bash
    python main.py
    ```
4.  O menu da aplicação será exibido, e você poderá interagir com as opções digitando o número correspondente.

## 📁 Estrutura do Projeto

```text
projeto-lista-de-afazeres/
│
├── main.py         # Arquivo principal, contém o menu e a lógica de navegação.
├── funcoes.py      # Contém as funções para adicionar, listar, atualizar e deletar tarefas.
└── tarefas.txt     # Arquivo de texto gerado automaticamente para armazenar as tarefas (criado na primeira adição de tarefa).
