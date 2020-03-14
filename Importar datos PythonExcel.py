"""
En este caso vamos a proceder a importar datos desde un fichero excel.
Para ellos al igual que hemos hecho con el caso de ficheros CSV, vamos a incluir tanto teoria como práctica.
"""
#Cargar fichero excel de manera rápida con read_excel

import pandas as pd
titanic_file = 'C\\.......'
data_titanic = pd.read_excel(titanic_file)

#Una vez cargado el fichero podemos proceder como con un fichero CSV con los metodos describe, dtypes,etc

#Pero la manera correcta de abrir un fichero excel y trabajar con el seria con las librerias de acontinuación
import xlrd
import xlwt
""" 
Vamos a explicar las funciones interesantes de estas librerias.
