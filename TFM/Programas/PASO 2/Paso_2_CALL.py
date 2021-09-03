#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 12:19:04 2021

@author: usuario
"""



import pandas as pd
import glob
from datetime import datetime
import mibian as mb
from datetime import date
import os
import shutil

#DATOS:------------------------------------------------------------------------
csv = glob.glob("C17*.csv")


#FUTUROS ----------------------------------------------------------------------
fut = pd.read_csv('/Users/usuario/Documents/MASTER/Datos_TFM/2017.csv')
fechas_futuros = pd.Series( fut.iloc[:,1] )
precio_futuro = pd.Series(fut.iloc[:,2])

'''
for i in range(len(csv)):
    preciof = []
    nom_fec = []
    nom_fec = csv[i][1:7]
    for j in range(len(fechas_futuros)):
        if nom_fec == str(fechas_futuros[j]):
            #print('if')
            preciof = precio_futuro[j]
        else:
            #print('else')
            j = j + 1
            
'''

# FECHAS DIFERENCIA + PRECIO + Strike ----------------------------------------------------------------


for j in range(len(csv)): 
    
    #Encontrar el precio del futuro para cada dia:
    preciof = []
    nom_fec = csv[j][-10:-4]
    for x in range(len(fechas_futuros)):
        if nom_fec == str(fechas_futuros[x]):
            preciof = precio_futuro[x]
        else:
            x = x + 1

    futuros = []
    fecha_inicial = []
    fecha_final = []
    fecha_diferencia = []
    precio = []
    p = []
    strike = []
    #nom_fec = csv[j][10:-4]
    tabla = pd.read_csv(csv[j])  
    #tabla.fillna("00,00" , inplace = True)
    
   
    for i in range(len(tabla.iloc[:,1])):
        #Fechas de compra:
        I_año = str(tabla.iloc[i , 1])[0:4]
        I_mes = str(tabla.iloc[i , 1])[4:6]
        I_dia = str(tabla.iloc[i , 1])[6:]
        #Fecha de expiracion
        F_año = str(tabla.iloc[i , 2])[0:4]
        F_mes = str(tabla.iloc[i , 2])[4:6]
        F_dia = str(tabla.iloc[i , 2])[6:]
        #calculo de las fechas:
        fecha_compra = date( int(I_año), int(I_mes), int(I_dia))
        fecha_expiracion = date(int(F_año), int(F_mes), int(F_dia))
        #diferencia:
        diferencia = (fecha_expiracion - fecha_compra).days
        #Introducimos las variables en listas:
        fecha_inicial.append(I_dia + "/" + I_mes + "/" + I_año) 
        fecha_final.append(F_dia + "/" + F_mes + "/" + F_año) 
        fecha_diferencia.append(diferencia)
        #extraccion del precio para poder usarlo como float:
        s = pd.Series ( str(tabla.iloc[i,4] ))
        a = s.str.split(pat=',' , expand=True)
        
        if a.shape == (1,1):
            p = float(tabla.Precio[i])
        else:
            p = float( str(a.iloc[0,0]) + '.' + str(a.iloc[0,1]) )
        
        #p = float(tabla.Precio[i])
        precio.append(p)
        #strike
        strike.append(float(tabla.iloc[i,3][4:9]))
        

        

    #ultimo dato que necesitamos de las tablas inciciales:
    contrato = tabla.iloc[: , 3]
    
    #Creamos el nuevo dataframe:
    df = pd.DataFrame()
    df.insert(0, 'Fecha Inicio', fecha_inicial , True)
    df.insert(1, 'Fecha Final', fecha_final , True)
    df.insert(2, 'Diferencia', fecha_diferencia , True)
    
    c =  pd.concat([df, contrato], axis=1)
    
    #datos del futuro:
    futuros = [preciof] * len(tabla)

    c.insert(4, 'Precio', precio , True)
    c.insert(5, 'Futuros' , futuros , True)
    c.insert(6, 's' , strike ,True)
   
    c.columns=['Fecha Inicio', 'Fecha Final', 'Diferencia' ,  'Contrato', 'Precio' , 'Futuro' , 'Strike']
    #nessmoney
    #data['moneyness'] = data.Strike/data.Futuro
    c['moneyness'] = c.Strike/c.Futuro
    
    #Limpiamos al maximo con filtro de dif y moneyness:
    # moneyness (0.9 , 1.2)
    # diferencia max 365
    #Filtramos que la diferencia de dias sea mayor que 0 sino mibian no puede funcionar:   
    filtro = c['Diferencia'] > 4
    c1 = c[filtro]
    c1.reset_index(inplace = True)
    c1 = c1.iloc[:,1:]
    
    filtro2 = c1['Diferencia'] < 400
    c2 = c1[filtro2]
    c2.reset_index(inplace = True)
    c2 = c2.iloc[:,1:]
    
    filtro3 = c2['moneyness'] >= 0.9
    c3 = c2[filtro3]
    c3.reset_index(inplace = True)
    c3 = c3.iloc[:,1:]
    
    filtro4 = c3['moneyness'] <= 1.2
    c4 = c3[filtro4]
    c4.reset_index(inplace = True)
    c4 = c4.iloc[:,1:]
    


    #Escribir lo csv
    c4.to_csv(csv[j][:-4] +  "_SEMIFINAL.csv")
    
    print(nom_fec  , "  Iteracion numero ---->" , j)
    

#mover os csv a una carpeta:
    
os.makedirs("/Users/usuario/Documents/MASTER/Datos_TFM/2017/RV/2017_CALLS/2017_SEMIFINAL_CALLS")     
csv_C = glob.glob("/Users/usuario/Documents/MASTER/Datos_TFM/2017/RV/2017_CALLS/C*_SEMIFINAL.csv")

for i in range(len(csv_C)):  
    shutil.move( csv_C[i] , "/Users/usuario/Documents/MASTER/Datos_TFM/2017/RV/2017_CALLS/2017_SEMIFINAL_CALLS")  
  

    
    
    
    