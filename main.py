from leituradedados import ler_dados_csv
from calculovendas import calcular_total_vendas

dados = ler_dados_csv('vendas.csv')
total = calcular_total_vendas(dados, chave_valor='valor')
print(f"Total de vendas: R${total:.2f}")