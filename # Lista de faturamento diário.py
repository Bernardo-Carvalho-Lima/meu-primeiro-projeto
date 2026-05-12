
# Lista de faturamento diário 
faturamento = [1500, 2300, 800, 4500, 1200, 3100, 500]

# 1. Calcule o faturamento total usando a função sum()
# A função sum() soma todos os valores da lista
total = sum(faturamento)

# 2. Calcular a média de faturamento
# len() retorna a quantidade de itens de uma lista
quantidade = len(faturamento)
# A média é o total dividido pela quantidade de dias
media = total / quantidade

# 3. Usar um laço FOR serve para identificar dias com faturamento acima da média
print(f"Relatório de Performance:")
# Mostra o faturamento total formatado com duas casas decimais
print(f"Faturamento Total: R$ {total:.2f}")
# Mostra a média diária formatada com duas casas decimais
print(f"Média Diária: R$ {media:.2f}")
# Linha separadora para organização visual
print("-" * 30)

# Percorre cada valor da lista de faturamento
for valor in faturamento:
    # Se o valor for maior que a média, destaca como positivo
    if valor > media:
        print(f"Destaque Positivo: R$ {valor} (Acima da média)")
    # Caso contrário, classifica como dia normal
    else:
        print(f"Dia Normal: R$ {valor}"
