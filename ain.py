import pandas as pd
import matplotlib.pyplot as plt

# --- Parte 2: Ler os Dados ---
dados = pd.read_csv("academia.csv")

# --- Parte 4: Estatísticas Básicas ---
# Criamos um DataFrame resumido para a tabela
tabela_resumo = dados[['Nome', 'Calorias', 'Peso', 'Idade']]

# --- Parte Bônus: Geração de TABELA para Entrega ---
fig, ax = plt.subplots(figsize=(10, 4)) # Ajusta o tamanho da imagem
ax.axis('tight')
ax.axis('off')

# Criando a tabela visual
tabela = ax.table(cellText=tabela_resumo.values, 
                  colLabels=tabela_resumo.columns, 
                  cellLoc='center', 
                  loc='center')

# Estilizando a tabela
tabela.auto_set_font_size(False)
tabela.set_fontsize(12)
tabela.scale(1.2, 1.2) # Ajusta o tamanho das células

plt.title('Tabela de Consumo de Calorias por Aluno', pad=20)

# Salva a tabela como imagem (em vez do gráfico)
plt.savefig('tabela_calorias.png', bbox_inches='tight', dpi=150)
print("\nArquivo 'tabela_calorias.png' gerado com sucesso!")

# Mostra na tela
plt.show()
