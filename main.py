import pandas as pd # importando a biblioteca pandas
import matplotlib as plt # importando a biblioteca matplotlib
import scipy import stats 
# modulo stats e possui funções estatísticas, como regressão linear 

#le o arquivo esv
# os dados serão armazenados pela variavel full_health_data
full_health_data = pd.read_csv("data.csv", header=0, sep=",")

# Selecionar a coluna do Datta frame 
# Essa coluna será usada como variavel
x = full_health_data["Average_pulse"]

y = full_health_data["Calorie_Burnage" ]
slope, intercept, r, p, std_err = stats.linregress(x, y)
