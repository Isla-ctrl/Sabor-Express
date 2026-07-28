import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
else:
    print(f'Erro ao obter dados da API: {response.status_code}')