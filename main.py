from exercicios_csv.ex01 import ler_dados_csv
from exercicios_csv.ex02 import filtrar_vendas_por_produto_input
from exercicios_csv.ex03 import calcular_total_vendas
from exercicios_csv.ex04 import gravar_resultados
from exercicicos_json.ex01 import carregar_dados_json

dados = ler_dados_csv('vendas.csv')
total = calcular_total_vendas(dados, chave_valor='valor')
lista = filtrar_vendas_por_produto_input(dados)

for dado in dados:
    print(dado)

for item in lista:
    print(item)

print(f"Total de vendas: R${total:.2f}")

gravar_resultados(total, lista)

dados_json = carregar_dados_json('dados.json')

print(dados_json)
for pessoa in dados_json['pessoas']:
    print(pessoa['nome'])

