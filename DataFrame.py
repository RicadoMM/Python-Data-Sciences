"""
<b>1. INTRODUCCIÓN A LOS DATA FRAME<\b>
Se trata de uno de los elementos mas empleados en el uso diario de Python, se puede definir a grandes rasgos como un conjunto de filas y de columnas
que se recogen en una tabla con o sin cabeceras y con indice.

Los dataFrame se pueden crear partiendo de diccinarios o de arrays creados con Numpy, asi como al realizar una consulta SQL contra SQL SERVER
o importando un fichero csv con pandas.read_csv, tambien al importar un fichero excel con pandas.read_excel.

El dataFrame se recoge dentro de la libreria Pandas y se puede entender como dijimos como una tabla, pudiendo recorrer sus filas, sus columnas,
pudiendo 

"""
#Creacion de un DataFrame vacío , solo especificamos las columnas, y los indices por los que vamos a clasificar nuestro DataFrame
#nos lo crea lleno de valores NaN
import pandas as pd
df = pd.DataFrama(columns=('Columna1','Columna2','Columna3'))

#Creacion de un DataFrame partiendo de un diccionario o de una serie de pandas
data = {'Lenguaje':['Python','C#','Java'],
       'Dificultad':['Media','Alta','Muy Alta'],
       'Ejecucion':['No compilado','Compilado','Compilado']}
df = pd.DataFrame(data)

#Partiendo de series de pandas
listado_lenguajes = ['Python','C#','Java']
d = {'Lenguaje': pd.series(['Sin compilar','Compilado','Compilado'],index = listado_lenguajes),
    'Dificultad': pd.series(['Media','Alta','Muy Alta'],index = listado_lenguajes)} 
#Si los indices no coincidieran lo que ocurre es que hay un merge y aparecen todos en el indice general del dataFrame, si resulta que una seria,
#no incluye ese indice aparecera como un NaN el valor asociado a ese indice en esa columna.
df = pd.DataFrame(d)

#Hasta aquí hemos creado de diferentes maneras DataFrames, recordar que los valores importados de un csv con read_csv o de un excel mediante read_excel
#asi como los valores importados con SQL pyodbc son mostrados o interpretados por python como un DataFrame, nosotros podemos crear un dataFrame mediante
#un csv unicamente seleccinando los datos que queremos mediante la creacion de un reader y seleccionando las filas.

#Creacion de un dataFrame con columnas seleccionadas -- en este caso solo lenguaje y dificultad
df = pd.dataFrame(data,columnas={'Lenguaje','Dificultad'})

#Podemos crear columnas nuevas de la siguiente manera.
df['Experiencia'] = 'variable asignar' #se crea todo la columna con la misma variable. Podemos hacerla condicional en funcion de otra del Data frame
df['Rentabilidad'] = df['Salario'] > 35000 #Todas las que cumplan con ese criterio en la columna Salario las indexará True en la nueva columna Rentabilidad.


#Borrar datos de DataFrame.
df.pop('Nombre Columna Borrar') #--> podemos alamacenarlo en una variable columna_borrada = df.pop('Nombre Columna Borrar')
del df['Nombre columna borrar'] # Hace lo mismo, borrar una columna.

#Insertar una columna.
salarios = pd.series([600000,350000,400000]) #--> se introduciria esta columna en nuestro dataframe.
df.insert(2,'Bien Pagado', salarios)

#Ordenar una DataFrame por indicce o por valor de columna.
df.sort_index(axis = 3,ascendig = false)
df.sort_values(by = 'Columna1')


"""
Vamos a ver como seleccionar columnas y filas mediante iloc, loc y ix.
 - iloc --> seleccionar datos mediante el número de la fila.
 - loc --> seleccioanr datos mediante el nombre de la cabecera de la columna un condicional.
 - ix --> una seleccion hibrida.
 
 Debemos de recordar que cada linea de un dataFrame representa un registro y que cada columna representaria una variable.
 1. Vamos a seleccionar datos mediante iloc.
 2. Mediante loc.
 3. Mediante ix.
"""
#Filas------------------
df.iloc[value] #Selecciona la fila del valor indicado
df.iloc[-value]#Selecciona por abajo las filas,   -1 es la ultima fila.
df.iloc[value:val]#Selecciona las filas entre ambos valores, incluida la primera hasta val - 1.
df.iloc[value,value1,value2]#Selecciona las filas indicadas en los valores.
#Columnas --------------------
df.iloc[:,value] #Selecciona la columna indica.
df.iloc[:,-value]#Selecciona columnas desde el final de los datos. -1 es la ultima columna.
df.iloc[:,[value1,value2,value3]]#Selecciona las columnas indicadas en los valores pasados.
#Seleccion multiple de columnas y de filas.
df.iloc[value,valuec]#Selecciona fila y columna indicada
df.iloc[:,value:valuec]#Selecciona todas las filas y las columnas indicadas solo incluida la primera hasta valuec - 1.
df.iloc[[value,value1,value2],[valuec,valuec1,valuec2]]#Selecciona las filas y columnas indicadas.
#No se trata de uno de los parametros mas usados, unicamente o mayor mente para seleccionar la primera fila.

#loc ---> podemos usarlo de dos maneras buscando el nombre del indice o de las columnas o mediante la seleccion de filas que cumplan un look up condicional.
#Ambos metodos comparten la misma sintaxis de seleccion de valores, por lo que no la detallaremos tanto.
df.loc['Python']#Selecciona la fila con el indice indicado.
df.loc[:,'Dificultad']#Selecciona todas las filas y la columna Dificultad.

#Lo interesante de este punto es la posibilidad de aplicar un look up condicional. Lo que se hace es pasar o un array o pandas serie de True or False al indexer del
#metodo de busqueda loc seleccionando las filas que tienen True asociado por el array.

df.lol[df['Dificultad'] == 'Media'] #Todas las filas que tengan Dificultad Media seran seleccionadas.
df.loc[df['Dificultad'] == 'Media' , 'Lenguaje']#Seleccionamos los valores de la columna Lenguaje que cumplen con el criterio.
df.loc[df['Dificultad'] == 'Media', 'Lenguaje:Salario']
#IMPORTANTE, CUANDO SELECCIONAMOS UNA UNICA COLUMNA SE NOS DEVUELVE UN PANDAS SERIES, SI SELECCIONAMOS VARIOS SE NOS DEVUELVE UN DATAFRAME
#PODEMOS CONSEGUIR SIEMPRE UN DATAFRAME UNICAMENTE INDICANDO LA COLUMNA ENTRE CORCHETES ['Lenguaje']

#VAMOS A INDICAR CRITERIOS COMUNES A LA HORA DE SELECCIONAR DATOS DE UN DATA FRAME PARA EL TRABAJO DE CAMPO.


# Select rows with first name Antonio, # and all columns between 'city' and 'email'
data.loc[data['first_name'] == 'Antonio', 'city':'email']
 
# Select rows where the email column ends with 'hotmail.com', include all columns
data.loc[data['email'].str.endswith("hotmail.com")]   
 
# Select rows with last_name equal to some values, all columns
data.loc[data['first_name'].isin(['France', 'Tyisha', 'Eric'])]   
       
# Select rows with first name Antonio AND hotmail email addresses
data.loc[data['email'].str.endswith("gmail.com") & (data['first_name'] == 'Antonio')] 
 
# select rows with id column between 100 and 200, and just return 'postal' and 'web' columns
data.loc[(data['id'] > 100) & (data['id'] <= 200), ['postal', 'web']] 
 
# A lambda function that yields True/False values can also be used.
# Select rows where the company name has 4 words in it.
data.loc[data['company_name'].apply(lambda x: len(x.split(' ')) == 4)] 
 
# Selections can be achieved outside of the main .loc for clarity:
# Form a separate variable with your selections:
idx = data['company_name'].apply(lambda x: len(x.split(' ')) == 4)
# Select only the True values in 'idx' and only the 3 columns specified:
data.loc[idx, ['email', 'first_name', 'company']]

































































































































