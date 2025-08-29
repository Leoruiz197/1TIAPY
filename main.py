from leitura_de_dados import ler_dados_csv
from calculo_vendas import calcular_total_vendas
from filtragem_por_produto import filtrar_vendas_por_produto


dados = ler_dados_csv('vendas.csv')
total = calcular_total_vendas(dados, chave_valor='valor')
print(f"Total de vendas: R${total:.2f}")