import pandas as pd
# --- Parte 2: Ler os Dados ---
dados = pd.read_csv("academia.csv")

# --- Parte 4: Estatísticas Básicas ---
# Criamos um DataFrame resumido para a tabela
print("="*30)
print("Base de Dados Completa")
print("="*30)
print(dados)
print("\n")

print("-" * 20)
print("Primeiras 5 Linhas:")
print(dados.head())

print("\n" + "-" * 20)
print("Ultimas 5 Linhas:")
print(dados.tail())

print("-" * 20)
print(f"Quantidade de(LINHAS, COLUNAS): {dados.shape}")

print("\n" + "=" * 30)
print("ESTATISTICAS")
print("\n" + "=" * 30)

print(f"Média das idades: {dados['Idade'].mean():1.f} anos")

print(f"Média de Calorias: {dados['Calorias'].mean():1.f} kcal")

print(f"Maior peso: {dados['Peso'].max()} kg")

print(f"Menor peso: {dados['Peso'].min()} kg")

print("=" * 30)
