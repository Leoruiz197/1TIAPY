from exercicios_csv.ex01 import ler_dados_csv
from exercicios_csv.ex02 import filtrar_vendas_por_produto_input
from exercicios_csv.ex03 import calcular_total_vendas
from exercicios_csv.ex04 import gravar_resultados

dados = ler_dados_csv('vendas.csv')
total = calcular_total_vendas(dados, chave_valor='valor')
lista = filtrar_vendas_por_produto_input(dados)

for dado in dados:
    print(dado)

for item in lista:
    print(item)

print(f"Total de vendas: R${total:.2f}")

gravar_resultados(total, lista)