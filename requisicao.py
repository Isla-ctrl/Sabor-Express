import json

import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            'nome': item['Name'],
            'preco': item['Price'],
            'descricao': item['Description']
        })

else:
    print(f'Erro ao obter dados da API: {response.status_code}')

for nome_do_restaurante, dados in dados_restaurante.items():
    ##with open serve para abrir um arquivo e garantir que ele será fechado corretamente após o uso, mesmo que ocorra uma exceção durante a execução do bloco de código. O 'w' indica que o arquivo será aberto no modo de escrita, ou seja, se o arquivo já existir, ele será sobrescrito. Se não existir, será criado.
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        ### json.dump é uma função da biblioteca json que converte um objeto Python em uma string JSON e grava essa string em um arquivo. O parâmetro indent=4 é usado para formatar a saída JSON com uma indentação de 4 espaços, tornando-a mais legível.
        json.dump(dados, arquivo_restaurante, indent=4)