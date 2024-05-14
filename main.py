from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


## alvo: tamanho da orelha, variavel: tamanho da pata

def processa_dataset():
    data = pd.read_csv('archive(1)/possum.csv', delimiter = ',')

    print(data.head())
    data.fillna(0, inplace=True)
    numeric_df = data.select_dtypes(include=['number'])

    fig, ax = plt.subplots(figsize = (12,8))
    sns.heatmap(numeric_df.corr(), cmap = 'Blues', linewidths=0.2, annot=True)
    
    #plt.show()
    return data

#***************************************************
#   Função para calcular o B1
#***************************************************
def calcula_B1(data):
    b1 = 0
    n = 0
    d = 0
    y_mean = data['earconch'].mean()
    x_mean = data['footlgth'].mean()
    
    for x, y in zip(data['footlgth'], data['earconch']):
        n += (x - x_mean)*(y - y_mean)
        d += (x - x_mean)**2
    
    b1 = n/d
    #print(b1)
    return b1
    
#***************************************************
#   Função para calcular o B0
#***************************************************
def calcula_B0(data):
    y_mean = data['earconch'].mean()
    x_mean = data['footlgth'].mean()
    b1 = calcula_B1(data)
    return y_mean - (b1*x_mean)

def calcula_y(data):
    b0 = calcula_B0(data)
    b1 = calcula_B1(data)
    
    x = data['footlgth'].values
    y = (b1 * x) + b0
    return y

#***************************************************
#   Função para calcular o RMSE
#***************************************************
def calcula_rmse(data):
    soma = 0
    for y, y_pred in zip(data['earconch'], data['earconch_pred']):
        soma += (y - y_pred)**2
    
    rmse= np.sqrt(soma/len(data))
    return rmse
    

def plota_grafico(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['footlgth'], data['earconch'], color='blue', label='Dados Originais')
    plt.plot(data['footlgth'], data['earconch_pred'], color='red', label='Linha de Regressão')
    plt.xlabel('FootLength')
    plt.ylabel('EarConch')
    plt.title('Regressão Linear Simples')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    data = processa_dataset()
    b1 = calcula_B1(data)
    b0 = calcula_B0(data)
    data['earconch_pred'] = calcula_y(data)
    plota_grafico(data)
    rmse = calcula_rmse(data)
    print(rmse)