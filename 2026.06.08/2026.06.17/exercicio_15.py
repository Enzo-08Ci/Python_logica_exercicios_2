"""
15. Mini Relatório de Vendas

Considere:

sales = [150, 320, 450, 210, 500]
Exiba:

Total vendido
Maior venda
Menor venda
Média de vendas
"""

sales = [150, 320, 450, 210, 500]

print("\n")

print(f'''

Total vendido: ${sum(sales):.2f}
Maior venda: ${max(sales):.2f}
Menor venda: ${min(sales):.2f}
Média de vendas: ${sum(sales) / len(sales):.2f}

''')