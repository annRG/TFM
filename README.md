# TFM
Programas utilizados para la realización del TFM

Este proyecto consta de dos partes:
1. Limpieza de datos del MEFF. 

  Cada año contine cinco archivos correspondientes a los 3 pasos que se explican en la memoria.
  El paso 1 es unico y los pasos 2 y 3 hay dos de cada , una para las calls y otro para las puts.

2. Redes neuronales.

  Tenemos un programa para la preparacion de los datos para estas redes como se explica en la memoria.
  Tenemos los distintos modelos de redes neuronales que se implementarón en el trabajo todas con el metodo de kfolds.
  
  SNN : Son las redes neuronales simples. Aparece comentado las lineas en la creacion del modelo se descomentaran según quieras realizar un modelo u otro.
  
  CONV : Son las redes neuronales convolucionales. Igual que en SNN hay codigo comentado se se descomentará si se quiere añadir las capas o no.
  
  FLATTEN : Son las redes neuronales hibridas que convinan primero las capas convlucionales y despues las capas simples.
  
  Procesado de datoas de NN : procesado de datos como se explica en la memoria.
  
  DATOS_X2,DATOS_Y2 : Archivos con todos los datos para entrenar el modelo sin dimension
  
  SSVI: representacion de la superficie de volatilidad con las predicciones y los datos reales.
