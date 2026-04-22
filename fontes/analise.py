import csv

valores = []

with open('../dados/vendas.csv', newline='', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        valores.append(float(linha['valor']))

total = sum(valores)
media = total / len(valores)
maior = max(valores)

print("📊 RELATÓRIO DE VENDAS")
print(f"Total de vendas: R$ {total}")
print(f"Média de vendas: R$ {media:.2f}")
print(f"Maior venda: R$ {maior}")
