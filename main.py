import csv

def ler_dados_csv(caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                dados.append(linha)
        return dados
    except FileNotFoundError:
        print(f"Arquivo {caminho_arquivo} não encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return []

# Exemplo de uso
caminho = 'seuarquivo.csv'
dados = ler_dados_csv(caminho)
print(dados)
