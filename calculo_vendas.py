def calcular_total_vendas(lista_dados, chave_valor='valor'):
    """
    Calcula o total das vendas a partir de uma lista de dicionários.
    
    :param lista_dados: lista de dicionários gerada pela função ler_dados_csv
    :param chave_valor: chave do dicionário que contém o valor da venda (padrão: 'valor')
    :return: soma total das vendas
    """
    total = 0.0
    for linha in lista_dados:
        try:
            total += float(linha[chave_valor])
        except KeyError:
            print(f"A chave '{chave_valor}' não existe no dicionário: {linha}")
        except ValueError:
            print(f"Valor inválido na linha: {linha[chave_valor]}")
    return total
