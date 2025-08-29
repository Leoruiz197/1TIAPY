import csv

def gravar_resultados(total_vendas,vendas_filtradas):
    with open('resultado_vendas.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([f"Total de vendas: R${total_vendas:.2f}"])
        writer.writerow(["Vendas filtradas:"])
        for item in vendas_filtradas:
            writer.writerow([item])
