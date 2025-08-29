import csv

def ler_dados_csv(arquivo_csv):
    """
    Lê um arquivo CSV e retorna uma lista de dicionários.
    Cada dicionário representa uma linha do CSV, usando os cabeçalhos como chaves.
    
    :param arquivo_csv: caminho para o arquivo CSV
    :return: lista de dicionários
    """
    lista_dados = []
    try:
        with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                lista_dados.append(dict(linha))
    except FileNotFoundError:
        print(f"Erro: o arquivo {arquivo_csv} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
    
    return lista_dados