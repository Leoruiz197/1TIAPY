from ex01 import ler_dados_csv
from ex02 import filtrar_vendas_por_produto_input
from ex03 import calcular_total_vendas
from ex04 import gravar_resultados



dados = ler_dados_csv('vendas.csv')
total = calcular_total_vendas(dados, chave_valor='valor')
lista = filtrar_vendas_por_produto_input(dados)

for dado in dados:
    print(dado)

for item in lista:
    print(item)

print(f"Total de vendas: R${total:.2f}")

gravar_resultados(total, lista)