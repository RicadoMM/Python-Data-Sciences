"""
Tenemos varias maneras de obtener datos de nuestras paginas Web, en este caso vamos a evaluar un fichero que se encuenra alojado en una pagina web
Se trata de un fichero que se encuentra en una url.
Por lo tanto tenemos diferentes fuentes de datos y por lo tanto diferentes metodos para tratarlos:
1.URL --> Empleamos request
2.API-RES --> Empleamos resquest mas protocolo http y sus derivados.
3.Datos que forman parte de una pagina --> BeautifulSoap
4.Datos que requieren iteracción --> Selenium


"""
import request
url = "http://www.mambiente.munimadrid.es//opendata//horario.txt"
resp = requests.get(url)
print(resp) --> nos dara un valor, que indicara si ha tenido exito la petición o no. 

"""
dentro de resp.response --> nos da el valor de la petición solicitada.

"""
patha = rutaCarpeta_donde_guardamos_fichero
with open(path + horario.txt + 'wb') as output:
  output.write(resp.content)
  
  """ 
  con esto hemos guardado el fichero que hemos descargado de la petición request.
  Acontinuacion recorremos los valores dentro del fichero descargado.

"""
import csv
import matplotlib.pyplot as plt
path_guardar = 'C:\\...\\BigDataPython-master\\'
font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }
vs =[]
horas =[]
with open(path_guardar + 'horario.txt') as csv_file:
    read_csv = csv.reader(csv_file,delimiter =',')
    for row in read_csv:
        if(row[0]+row[1]+row[2]== '28079008' and row[3] == '12'):
            plt.title("Oxido Nitrigo :  "+ row[8]+" /"+ row[7]+"/"+row[6],fontdict=  font)
            hora = 0
            desp= 9
            
            while hora<=23:
                if row[desp+2*hora+1]=='V':
                    vs.append(row[desp+2*hora])
                    horas.append(hora)
                hora +=1
               
plt.plot(horas,vs)
plt.show()
"""
Debemos de mencionar que tenemos varios metodos para poder hacer peticiones a nuestra web
Una de ellas es la que hemos mostrado, es la más útil --> request.get / request.pos....
La otra se trata con la libreria urllib3 ya que estamos trabajando con python3

"""

import urllib3
http = urllib3.PoolManager()
response = http.request('GET',url)
resultado = response.status

"""
Vamos analizar otro ejemplo con urllib3
Tenemos que mencionar que PoolManager gestiona por nostros los hilos de ejecucion.
Podemos crearlo como:
  http = PoolManager(10) --> creando asi la opcion de realizar varias peticiones a la vez sobre una página.
  respone = http.request('GET',URL)
    
"""
import urllib3
http = urllib3.PoolManager() 
r = http.request('GET',url) #se trata de un string binario y tenemos que decodificarlo , por eso tambien en el metodo de arriba hacemos
#open(path,'wb') que indica que se abre un fichero para escribir en formato binario, por eso no tenemos que decodificarlo, b indica binario,
# w,r,a sin la b indica que no es binario. Si no es binario lo que obtenemos desde web debede de decodificarse con decode('utf-8')
data=r.data
str_data = data.decode('utf-8')
lineas = str_data.split('\n')# con ello dividimos nuestro array en filas separandolo con intros.
nombre_columnas = lineas[0].strip().split(',')
n_cols = len(nombre_columnas)
#Creamos un diccionario para almacenar clave valor los datos obtenidos de las URL
contador = 0
diccionario = {}

for col in nombre_columnas:
  diccionario[col] = {} #Introducimos la clave que sera el nombre de la columna
  
 #Recorremos linea a linea el fichero y lo vamos introduciendo en el diccionario en funcion a la columna que corresponde.
for linea in lineas:
  if counter>0:
    values = linea.strip().split(',')
    for i in range(len(nombre_columnas)):
      diccionario[nombre_columnas[i]].append(values[i])
      #tambien se podria hacer
      # diccionario[nombre_columnas[i]] = values[i]
      contador +=1
      
  #Una vez cargados los datos en nuestro diccionario creamos un dataFrame
  
 dFrame = pd.DataFrame(diccionario) #En caso de que no tuviera la fila de cabeceras las podemos introducir mediante columns ={'Nombre1','Nombre2'}
#FINALMENTE GUARDAMOS LOS DATOS
dFrame.to_csv(path)
dFrame.to_excel(path)
dFrame.to_json(path)
#Esas son las acciones posibles de mostar los datos luego en un fichero.
#Una vez que tenemos los datos cargados en un fichero csv podemos usar las tecnicas de DataWrangling




