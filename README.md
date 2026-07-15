# 🍽️ Sabor Express

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen?style=for-the-badge)
![Alura](https://img.shields.io/badge/Curso-Alura-blueviolet?style=for-the-badge)

Sistema de cadastro e gerenciamento de restaurantes, desenvolvido em Python durante a carreira de Backend em Python na Alura.

Este repositório reúne **duas versões do mesmo projeto**, feitas em momentos diferentes do curso:

- **`logica-de-programacao`** → primeira versão, construída com lógica de programação básica (funções, listas de dicionários, laços, condicionais).
- **`orientacao-a-objetos`** → mesmo projeto reconstruído do zero aplicando Programação Orientada a Objetos, avançando depois para consumo e criação de APIs.

A ideia de manter as duas pastas no mesmo repositório é justamente deixar visível a evolução: o mesmo problema (gerenciar restaurantes) resolvido com abordagens diferentes, conforme fui avançando no curso.

---

## 📁 Parte 1 - Lógica de Programação

Sistema de cadastro e gerenciamento de restaurantes rodando via terminal (CLI).

O app simula um painel simples de administração: cadastra restaurantes, lista todos os cadastrados, alterna entre ativo/inativo e sai do sistema, tudo através de um menu interativo no terminal.

### Funcionalidades
- **Cadastrar restaurante** - registra nome e categoria, com status inicial `inativo`.
- **Listar restaurantes** - exibe uma tabela formatada com nome, categoria e status (ativado/desativado).
- **Alternar estado do restaurante** - busca por nome e inverte o status entre ativo/inativo.
- **Sair do app** - encerra o programa com uma mensagem de finalização.
- Validação de opções inválidas, com tratamento de erros via `try/except`.
- Menu que se reinicia automaticamente após cada ação, sem precisar rodar o script de novo.

### Conceitos e habilidades praticados
- **Estruturas de dados**: lista de dicionários para representar os restaurantes (`nome`, `categoria`, `ativo`), e como acessar/alterar valores dentro dela.
- **Funções**: separação do código em funções pequenas e específicas (`cadastrar_novo_restaurante`, `listar_restaurantes`, `alternar_estado_do_restaurante` etc.), cada uma com uma responsabilidade só.
- **Docstrings**: documentação das funções explicando inputs e outputs, como boa prática de legibilidade.
- **F-strings** para interpolar variáveis em mensagens.
- **Formatação de texto no terminal**: uso de `.ljust()` para alinhar colunas na listagem, deixando a "tabela" legível.
- **Controle de fluxo**: `if/elif/else`, laços `for` e expressões condicionais em uma linha.
- **Tratamento de exceções** com `try/except` para evitar que o programa quebre com entradas inválidas.
- **Módulo `subprocess`** para limpar o terminal (`subprocess.run('cls', shell=True)`) e deixar a interface mais limpa a cada tela.
- **Recursão prática**: as funções `reiniciar()` e `main()` se chamam entre si para manter o loop do menu rodando.
- **Exploração de sintaxe alternativa**: testei a estrutura `match/case` do Python (equivalente a um `switch`) como alternativa ao `if/elif`, deixada comentada no código como registro de estudo e comparação entre abordagens.

**Tecnologias:** Python 3 · Módulo `subprocess` (biblioteca padrão)

---

## 📁 Parte 2 - Programação Orientada a Objetos

Mesmo projeto de gerenciamento de restaurantes, reconstruído aplicando Programação Orientada a Objetos, e depois expandido para consumir e criar APIs.

### Funcionalidades
- Cadastro de restaurantes representado por uma classe `Restaurante`, com atributos de instância (nome, categoria, status ativo/inativo).
- Cardápio próprio por restaurante, com itens que podem ser `Prato` ou `Bebida`, herdando de uma classe base `ItemCardapio`.
- Sistema de avaliações: cada restaurante mantém uma lista de objetos `Avaliação` associados a ele.
- Aplicação de descontos nos itens do cardápio, com comportamento diferente para bebidas e pratos (polimorfismo).
- Consumo de uma API externa de restaurantes via `requests`, salvando os dados recebidos em arquivos JSON.
- Criação de uma API própria com **FastAPI**, com endpoints para consultar e filtrar restaurantes, e documentação automática (`/docs` e `/redoc`).

### Conceitos e habilidades praticados

**Fundamentos de POO**
- Classe como estrutura que define um tipo específico de objeto, e importância das classes para organizar código de forma modular e reutilizável.
- Construtor `__init__`, responsável por inicializar os atributos da instância (incluindo valores padrão, como `ativo = False`).
- Diferença entre atributos de classe e atributos de instância.
- Atributos protegidos (prefixo `_`) e uso do decorator `property` para controlar o acesso e a leitura de atributos como `categoria` e `ativo`.
- Métodos de classe (`classmethod`), por exemplo, `listar_restaurantes`, que age sobre a classe como um todo em vez de uma instância específica.
- Docstrings: quando vale a pena documentar (código destinado a ser compartilhado com outros devs) e quando não é necessário (código simples, autoexplicativo, ou projetos pessoais de curto prazo).

**Relacionamento entre classes**
- Importação de classes entre arquivos Python (ex: importar `Restaurante` para o `main.py`), permitindo modularizar o projeto.
- Composição/associação entre classes: relação entre `Restaurante` e `Avaliação`, com uma lista de avaliações vinculada a cada restaurante.

**Herança e Polimorfismo**
- Criação da classe base `ItemCardapio` (com `nome` e `preço`) e das subclasses `Bebida` e `Prato`, que herdam dela usando `super()` no construtor.
- Refatoração do método de adicionar itens ao cardápio para aceitar qualquer instância de `ItemCardapio`.
- Uso de `property` para exibir o cardápio de cada restaurante.
- Método abstrato `aplicar_desconto`, aplicado de forma diferente em `Bebida` e `Prato`, prática de polimorfismo: classes diferentes respondendo ao mesmo método de maneiras distintas.

**Ambientes e boas práticas**
- Ambientes virtuais (`venv`): criação e ativação, isolando dependências de cada projeto e evitando conflitos entre versões de bibliotecas.
- Criação e uso de `requirements.txt` para documentar e compartilhar as dependências do projeto, garantindo reprodutibilidade em outras máquinas.

**Consumo de API**
- Conceito de API como ponte entre sistemas, permitindo comunicação e compartilhamento de dados.
- Uso do módulo `requests` para fazer requisições a uma API de restaurantes e receber informações em formato JSON.
- Salvamento dos dados recebidos em arquivos JSON, para armazenamento local e uso futuro.
- Criação manual de arquivos JSON próprios, entendendo como estruturar e organizar dados em um formato legível e interoperável.

**Criação de API própria (FastAPI)**
- Instalação e configuração do **FastAPI** para criar uma API em Python.
- Criação de endpoints para disponibilizar recursos relacionados aos restaurantes.
- Uso de query parameters para filtrar restaurantes por nome.
- Geração automática de documentação interativa da API com `docs` e `redoc`, permitindo testar os endpoints diretamente pela interface.

**Tecnologias:** Python 3 · `requests` · `FastAPI` · `venv`

---

## 👩‍💻 Autora

Desenvolvido durante meus estudos de Python, do primeiro contato com lógica de programação até a aplicação de Orientação a Objetos e consumo/criação de APIs.

> O mais importante foi me desafiar a estruturar o código antes de ver a resolução dos instrutores, mesmo que isso torne meus estudos mais longos. Mas o mais importante para mim é desenvolver uma base sólida e futuramente ser capaz de sustentar cada conhecimento. Não é preciso decorar tudo, mas sim, saber pesquisar e ter a paciência de pensar na resolução do problema.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/https://www.linkedin.com/in/beatriz-souza-6a942b333/)


