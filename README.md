# 🍽️ Sabor Express

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen?style=for-the-badge)
![Alura](https://img.shields.io/badge/Curso-Alura-blueviolet?style=for-the-badge)

Sistema de cadastro e gerenciamento de restaurantes rodando via terminal (CLI), desenvolvido em Python, durante a carreira de Backend em Python na Alura.

O app simula um painel simples de administração: cadastra restaurantes, lista todos os cadastrados, alterna entre ativo/inativo e sai do sistema — tudo através de um menu interativo no terminal.

---

## 🎯 Funcionalidades

- **Cadastrar restaurante** — registra nome e categoria, com status inicial `inativo`.
- **Listar restaurantes** — exibe uma tabela formatada com nome, categoria e status (ativado/desativado).
- **Alternar estado do restaurante** — busca por nome e inverte o status entre ativo/inativo.
- **Sair do app** — encerra o programa com uma mensagem de finalização.
- Validação de opções inválidas, com tratamento de erros via `try/except`.
- Menu que se reinicia automaticamente após cada ação, sem precisar rodar o script de novo.

---

## 🧠 Conceitos e habilidades praticados

Esse projeto foi minha porta de entrada na lógica de programação com Python. Alguns dos principais aprendizados:

- **Estruturas de dados**: lista de dicionários para representar os restaurantes (`nome`, `categoria`, `ativo`), e como acessar/alterar valores dentro dela.
- **Funções**: separação do código em funções pequenas e específicas (`cadastrar_novo_restaurante`, `listar_restaurantes`, `alternar_estado_do_restaurante` etc.), cada uma com uma responsabilidade só.
- **Docstrings**: documentação das funções explicando inputs e outputs, como boa prática de legibilidade.
- **F-strings** para interpolar variáveis em mensagens (`f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!'`).
- **Formatação de texto no terminal**: uso de `.ljust()` para alinhar colunas na listagem, deixando a "tabela" legível.
- **Controle de fluxo**: `if/elif/else`, laços `for` e expressões condicionais em uma linha (`'ativado' if restaurante['ativo'] else 'desativado'`).
- **Tratamento de exceções** com `try/except` para evitar que o programa quebre com entradas inválidas.
- **Módulo `subprocess`** para limpar o terminal (`subprocess.run('cls', shell=True)`) e deixar a interface mais limpa a cada tela.
- **Recursão prática**: as funções `reiniciar()` e `main()` se chamam entre si para manter o loop do menu rodando.
- **Exploração de sintaxe alternativa**: cheguei a testar a estrutura `match/case` do Python (equivalente a um `switch`) como alternativa ao `if/elif`, deixada comentada no código como registro de estudo e comparação entre abordagens.

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Módulo `subprocess` (biblioteca padrão)

---

## 👩‍💻 Autora

Desenvolvido por **Isla** durante meus estudos de Python.

[![GitHub](https://img.shields.io/badge/GitHub-Isla--ctrl-181717?style=for-the-badge&logo=github)](https://github.com/Isla-ctrl)
