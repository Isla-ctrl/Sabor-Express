from fastapi import FastAPI, Query

import requests

app = FastAPI()

##@app significa que a função hello_world é uma rota da API, e o caminho da rota é /api/hello. Quando o usuário acessar esse caminho, a função hello_world será executada e retornará um dicionário com a mensagem "Hello": "World!".
@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe uma mensagem incrível do mundo da programação!
    
    '''
    return {'Hello': 'World!'}


@app.get('/api/restaurantes')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardápios dos restaurantes  
    
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    if restaurante is None:
        return {'Dados': dados_json}

    dados_restaurante = []
    for item in dados_json:
        if item['Company'] == restaurante:
            dados_restaurante.append({
                'nome': item['Name'],
                'preco': item['Price'],
                'descricao': item['Description']
            })
    return {'Restaurante':restaurante, 'Cardápio': dados_restaurante}

else:
    return {'Erro': f'{response.status_code} - {response}'}
