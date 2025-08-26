import csv
from typing import List, Dict

caminho_arquivo = "dados.csv"

def ler_dados_csv(caminho_arquivo) -> List[Dict[str, str]]:

    with open(caminho_arquivo, newline="", encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f, delimiter=",")
        return [dict(row) for row in reader]

# Chamada da função
dados = ler_dados_csv(caminho_arquivo)

# Visualizar resultado
print(dados)
