def filtrar_vendas_por_produto_input(lista_dados, chave_produto='produto'):
    """
    Filtra as vendas de um produto específico fornecido pelo usuário.
    
    :param lista_dados: lista de dicionários gerada pela função ler_dados_csv
    :param chave_produto: chave do dicionário que contém o nome do produto (padrão: 'produto')
    :return: lista de dicionários com as vendas do produto especificado
    """
    nome_produto = input("Digite o nome do produto que deseja filtrar: ").strip()
    
    vendas_filtradas = [linha for linha in lista_dados if linha.get(chave_produto) == nome_produto]
    
    if not vendas_filtradas:
        print(f"Nenhuma venda encontrada para o produto '{nome_produto}'.")
    
    return vendas_filtradas
