#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 11:47:15 2021

@author: usuario
"""

import pandas as pd
import mibian_mod as mibian # mod version with less iters: result is almost identical
import glob
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import shutil
import os


csv = glob.glob("C17*_SEMIFINAL.csv")

'''

for j in range(len(csv)): 
    
    nom_fec = csv[j][:7]
    data = pd.read_csv(csv[j])  
    
    #ordenamos los datos:
    data.sort_values(['Diferencia', 'moneyness'])
    data.Precio.fillna( method='bfill')
    data.Precio.fillna( method='ffill')
   
    #calculo de volatilidad
    n = data.shape[0]
    for i in range(n):
        one_option = data.iloc[i]
    
        underlyingPrice = one_option.Futuro
        strike =  one_option.Strike
        interestRate = 0.001
        annualDividends = 0.02
        daysToExpiration = one_option.Diferencia
        callPrice = one_option.Precio
    
        #data_mibian = [underlyingPrice, strike, interestRate, annualDividends, daysToExpiration]
        data_mibian_bs = [underlyingPrice, strike, interestRate, daysToExpiration]
        #obj_mibian = mibian.Me(data_mibian, putPrice=callPrice)
        obj_mibian = mibian.BS(data_mibian_bs, callPrice=callPrice)
        vola = obj_mibian.impliedVolatility
        #print(f'{i}/{n}')
        #print(f"{data_mibian_bs} {callPrice} {vola}")
        data.loc[one_option.name, 'new_vola'] = vola
        
    #tenemos que tener el data frame rellenito:
    #Primero forzamos los nan de los 0.001:
    data['new_vola'] = data['new_vola'].replace(0.001 , np.nan)
    #ahora rellenamos con el primer o ultimo valor posible:
    prueva = data.fillna(axis=0, method='bfill')
    final = prueva.fillna(axis=0, method='ffill')
    
    
    
    #grafica superficie:  
    calls_volatilit = final.set_index(['Diferencia', 'moneyness'])['new_vola'].unstack(level=-1)
    #tieen que estar copletos los valores
    calls_volatilit = calls_volatilit.fillna(axis=1, method='bfill')
    calls_volatilit = calls_volatilit.fillna(axis=1, method='ffill')
    
    if j!=0 and 10%j == 0:
        x = calls_volatilit.index.values
        y = calls_volatilit.columns.values
        z = calls_volatilit.values
    
    
        fig = plt.figure(figsize=(20, 20))
        ax = plt.axes(projection='3d')
        X, Y = np.meshgrid(x, y)
        ax.plot_surface(X, Y, z.T)
        ax.set_xlabel('Days', fontsize=14)
        ax.set_ylabel('Moneyness', fontsize=14)
        ax.set_zlabel('$\sigma$', fontsize=14)
        ax.set_title('Dia '+ csv[j][5:7]+ ' del ' + csv[j][3:5]+ ' del 20'+csv[j][1:3], fontsize=20)
        #plt.savefig("./figures/figure{0:03d}.png".format(i))
    
    

    #Escribir lo csv
    final.to_csv(csv[j][:7] +  "_FINAL.csv")
    
    print(nom_fec  , "  Iteracion numero ---->" , j)
'''   

#mover os csv a una carpeta:
    
os.makedirs("/Users/usuario/Documents/MASTER/Datos_TFM/2017/RV/2017_CALLS/2017_SEMIFINAL_CALLS/2017_FINAL_CALLS")     
csv_C = glob.glob("/Users/usuario/Documents/MASTER/Datos_TFM/2017/RV/2017_CALLS/2017_SEMIFINAL_CALLS/C*_FINAL.csv")

for i in range(len(csv_C)):  
    shutil.move( csv_C[i] , "/Users/usuario/Documents/MASTER/Datos_TFM/2017/RV/2017_CALLS/2017_SEMIFINAL_CALLS/2017_FINAL_CALLS")  
  

    
