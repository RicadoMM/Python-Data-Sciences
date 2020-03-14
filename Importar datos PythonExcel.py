"""
En este caso vamos a proceder a importar datos desde un fichero excel.
Para ellos al igual que hemos hecho con el caso de ficheros CSV, vamos a incluir tanto teoria como práctica.
"""
#Cargar fichero excel de manera rápida con read_excel

import pandas as pd
titanic_file = 'C\\.......'
data_titanic = pd.read_excel(titanic_file,'Nombre Hoja')

#Una vez cargado el fichero podemos proceder como con un fichero CSV con los metodos describe, dtypes,etc

#Pero la manera correcta de abrir un fichero excel y trabajar con el seria con las librerias de acontinuación
import xlrd
import xlwt
""" 
Vamos a explicar las funciones interesantes de estas librerias.
  - Clase Workbook 
        open_workbook(ruta) --> libro para poder trabajar con el.
        nsheets --> devuelve el número de hojas que tiene nuestro libro.
        sheet_by_index(index) --> nos devuelve un objeto hoja.
        sheet_names --> devuelve los nombres de las hojas.
  - Clase Sheet , reprensentan las hojsa, no pueden ser cargados de manera própia, deben de derivar de un libro.
        ncols & nrows --> devuelve el nºde columnas y nºde filas respectivamente.
        name --> devuelve el nombre de la hoja.
        cells(filx,cols) --> devuelve un objeto Celda.
        col(colx) --> una lista iterable con todos los valores de la columna.
        row(rowx) --> una lista iterable con todos los valores de la fila.
  - Clase Cell , representa un objeto del tipo Cell que debe de derivar de un obeto Sheet. Contiene el valor de la celda, el tipo de valor
    y el formato de la celda.
        ctype -> tipo de valor de la celda 0 = celda vacia, 1 = str , 2 = número , 3 = fecha , 4 = Booleano (1 true,0 false) 5 error, 6 valor vacio excel
        value --> devuelve el valor.
        colname(c)--> nombre la columna, es decir colname(2) = B
        
        
"""
import xlrd
import xlwt
listado_valores = [] # no confundir con un diccionario que se declara con {}
with xlrd.open_workbook(ruta) as libro_excel:
  n_hojas = libro_excel.nsheets
  if n_hojas == 3:
    for hojas in libro_excel.sheets:
      if hojas.name == 'Hoja1':
        n_filas = hojas.nrows
        n_columnas = hojas.ncols
        for i in range(1,n_cols):
          for j in range(1,n_filas):
            fila = hojas.row[j]
            valor_celda = filas[0] #estamos cogiendo la primera columna con respecto a la primera fial
            if valor_celda not in listado_valores:
              listado_valores.append(valor_celda)
           
          
 print(listado_valores)
"""
De esta manera hemos recorrido todas las filas y todas las columnas de nuestro fichero excel que hemos cargado.
Para crear un fichero excel deberemos de hacer uso de nuestra libreria xlwt como veremos en el ejemplo.
"""
import xlrd
import xlwt

libro_escribir = xlwt.Workbook()






