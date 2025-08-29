import json

def carregar_dados_json(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    return dados