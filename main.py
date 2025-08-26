import csv

def read_csv_to_dicts(file_path):
    """
    Lê um arquivo CSV e retorna uma lista de dicionários.
    Cada dicionário representa uma linha com cabeçalhos como chaves.
    
    Args:
        file_path (str): Caminho do arquivo CSV
        
    Returns:
        list: Lista de dicionários com os dados do CSV
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            return [dict(row) for row in csv_reader]
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_path}' não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {str(e)}")
        return []

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de caminho para o arquivo CSV
    file_path = "exemplo.csv"
    
    # Lê o CSV e obtém a lista de dicionários
    data = read_csv_to_dicts(file_path)
    
    # Imprime o resultado
    for row in data:
        print(row)