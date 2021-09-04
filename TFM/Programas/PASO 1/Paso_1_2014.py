#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 19:55:36 2021

@author: usuario
"""



import pandas as pd
import zipfile
import glob
import os
import numpy as np
import shutil





ruta_zip = glob.glob('/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/MEFF_2014*.zip')
#print(ruta_zip)

ruta = glob.glob('/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/MEFF_2014*.zip')

nombres = []


#for i in range(len(ruta)):
    



for i in range(len(ruta_zip)):
    nombres.append(ruta[i][-10:-4])
    print( nombres[i] , "  Iteracion numero ---->" , i)
    #Creamos la carpeta temporal para las descompresiones:
    os.makedirs("/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/temporal")         
    
    #Desocmprimimos el primer archivo dentro de la temporal y el segundo ya en este directorio:
    archivo_zip = zipfile.ZipFile( ruta_zip[i] , "r")
    archivo_zip.extractall(pwd=None, path="/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/temporal")
    
    #leemos la tabla que nos interesa:
    tabla_precio = pd.read_table( '/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/temporal/CCONTRSTAT.c2', sep=";",header=None, names=None , index_col=None  ) 
    precio = tabla_precio.iloc[:,7]
    contratoP = tabla_precio.iloc[:,2]
    #guardamos la tabla en el directorio principal:
    #tabla_precio.to_csv(nombres[i] + ".csv")
    
    tabla_otra = pd.read_table( '/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/temporal/CCONTRACTS.C2', sep=";" ,header=None, names=None , index_col=None ) 
    fecI = tabla_otra.iloc[:,0]
    fecF = tabla_otra.iloc[:,6]
    contrato1 = tabla_otra.iloc[:,2]
    #HAcer mi nuevo data frame
    #primero las de otro:
    a =  pd.concat([fecI, fecF], axis=1)
    b =  pd.concat([a, contrato1], axis=1)
    b.columns=['Fecha Inicio', 'Fecha Final',  'Contrato']
    #ahora las d eprecio:
    c =  pd.concat([contratoP, precio], axis=1)
    c.columns=['Contrato' , 'Precio']
    #join de ambas tablas por contrato:
        
    df_final = pd.merge(b, c, on='Contrato',how='outer')
    
    
    ibex_call = df_final[df_final.Contrato.str.contains('CIBX', regex=True)] 
    ibex_call.reset_index(drop=True , inplace = True) #resear el indice
    ibex_call.columns=['Fecha Inicio', 'Fecha Final',  'Contrato', 'Precio']
    df_ibex_call = ibex_call[['Fecha Inicio','Fecha Final','Contrato','Precio']]
    
    
    ibex_put = df_final[df_final.Contrato.str.contains('PIBX', regex=True)] 
    ibex_put.reset_index(drop=True , inplace = True) #resear el indice
    ibex_put.columns=['Fecha Inicio', 'Fecha Final',  'Contrato', 'Precio']
    df_ibex_put = ibex_put[['Fecha Inicio','Fecha Final','Contrato','Precio']]
    
  
    #guardamos la tabla en el directorio principal:
    #df_final.to_csv(nombres[i] + ".csv")
    df_ibex_put.to_csv('P' + nombres[i] + ".csv")
    df_ibex_call.to_csv('C' + nombres[i] + ".csv")
    

    #eliminar la careta con todo dentro:
    shutil.rmtree("/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/temporal")
  
    

#mover os csv a una carpeta:
os.makedirs("/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/2014_CALLS")     
os.makedirs("/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/2014_PUTS")      
csv_C = glob.glob("/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/C*.csv")
csv_P = glob.glob("/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/P*.csv")

for i in range(len(csv_P)):  
    shutil.move( csv_C[i] , "/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/2014_CALLS")   
    shutil.move( csv_P[i] , "/Users/usuario/Documents/MASTER/Datos_TFM/2014/FichWeb_2014/RV/2014_PUTS")              

