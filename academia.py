import pandas as pd
import matplotlib.pyplot as plt

# --- Parte 2: Ler os Dados ---
dados = pd.read_csv("academia.csv")
print("--- TABELA COMPLETA ---")
print(dados)
print("-" * 30)

# --- Parte 3: Exploração Inicial (Exercício 1) ---
print("\n--- EXERCÍCIO 1: EXPLORAÇÃO ---")
print("Primeiras 5 linhas:")
print(dados.head())

print("\nÚltimas 5 linhas:")
print(dados.tail())

print("\nQuantidade de (linhas, colunas):")
print(dados.shape)
print("-" * 30)

# --- Parte 4: Estatísticas Básicas (Exercício 2) ---
print("\n--- EXERCÍCIO 2: ESTATÍSTICAS ---")
print(f"Média das idades: {dados['Idade'].mean():.2f} anos")
print(f"Média das calorias gastas: {dados['Calorias'].mean():.2f} kcal")
print(f"Maior peso registrado: {dados['Peso'].max()} kg")
print(f"Menor peso registrado: {dados['Peso'].min()} kg")
print("-" * 30)

# --- Parte Bônus: Geração de Gráfico para Entrega ---
# Vamos criar um gráfico simples de Horas de Treino vs Calorias
plt.figure(figsize=(10, 6))
plt.bar(dados['Nome'], dados['Calorias'], color='skyblue')
plt.title('Calorias Gastas por Aluno')
plt.xlabel('Alunos')
plt.ylabel('Calorias (kcal)')
plt.xticks(rotation=45)
plt.tight_layout()

# Salva o gráfico como imagem
plt.savefig('grafico_calorias.png')
print("\nGráfico 'grafico_calorias.png' gerado com sucesso!")

# Mostra o gráfico na tela
plt.show()