"""
En este punto vamos a tratar las conexiones a BBDD, en primer lugar a SQL, pero mas a delante lo haremos a MongoDB y PostgreSQL.
Por lo tanto para comenzar con este apartado, empecemos introduciendo SQL.

SQL se trata de una BBDD o un motor de BBDD de caracter relacional, es decir, nuestros datos se encuentran alojados en SQL relacionandose entre si.
Para mas conceptos de SQL, como aspectos tecnicos, teoria propia de este lenguaje de consultas, etc mirar otro articulo colgado en mi repositorio donde se aborda exclusivamente SQL.

"""
"""
Lo que hacemos es conectarnos a la API de SQL para realizar las consultas necesarias.
Por lo tanto desde la aplicacion de programa tenemos las siguientes acciones:
  1. Connectarnos a la BBDD --> CONNECT(db,user name,pswd)
  2. Mandar datos como consulta --> SEND("update employees set.....")
  3. Ejecutar consulta --> EXECUTE()
  4. Comprobar status --> STATUS CHEC()
  5. Si STATUS = OK DISCONNECT()
  
  Conectos diferenciados:
  1. Objetos de connexion --> connectarnos a BBDD y configurar transacciones
  2. Objetos de cursor --> para las queries en la BBDD. Para poder recorrer los resultados de una consulta.
  
  Metodos que se emplean normalmente junto con los objetos de conexion
  1. cursor() --> devuelve un nuevo objeto cursor de una conexion existente.
  2. commit() --> ejecuta cualquier consulta pendiente de relizar con la BBDD.
  3. rollback() --> 
  4. close() --> cerrar la conexión.
 
  Finalmente indicamos la libreria a emplear pyodbc.
  """
  import pyodbc
  #server = 'localhost\sqlexpress'
  #database = 'nombre de bbdd'
  #username = 'nombre de usuario'
  #password = 'contraseña'
  try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 19 for SQL Server};SERVER' + server +
                        ';DATABASE='+database+';UID='+username+';PWD='+password)
    except Exception as e:
      print('Se ha producio un error con la conexión a la BBDD: ",e)
  #Obtenemos ahora el cursor de la conexion creada
  cursor = conexion.cursor#Si usamos el concepto de with no necesitamos declararlo antes.
 try:
 with conexion.cursor() as cursor:#Esta opción nos cierra automaticamente el cursor sin tener que hacer cursor.close()
    
    consulta = 'INSERT INTO tabla_1(nombre,edad) VALUES (?,?);"
    cursor.Execute(consulta_sql,('Ricardo','15'))
  except Exception as e:
  print('Se ha producido un error durante la querie :" ,e)
  finally:
    conexion.close() #Una vez que terminamos de trabajar debemos de cerrar la conexión con nuestra BBDD ya que si no estamos perdiendo memoria ram
  
  
  #VAMOS A SELECCIONAR DATOS DESDE UNA TABLA.
  with conexion.cursor() as cursor:
    cursor.execute("SELECT ID, NOMBRE,EDAD FROM tabla_1;")
    persona = cursor.fetchall() #Con fetchall nos traemos todas las filas de nuestra consulta. Es un iterable(listado)
    for per in persona:
      print(per)
      
  
  #PODEMOS RECORRER LAS FILAS MIENTRAS SE REGRESE ALGUN VALOR, Y NO GUARDAR TODO EN UNA LISTA E ITERAR ESA LISTA.
  
  with conexion.cursor() as cursor:
    cursor.execute("SELECT ID,CIUDAD,SEXIO FROM TABLA_2;")
    personas = cursor.fetchone()
    while personas:
      print(personas)
      personas = cursor.fetchone()
      
      
   #CONSULTA CON WHERE Y LIKE
    
    with conexion.cursor() as cursor:
      consulta = 'SELECT * FROM TABLA_2 WHERE CIUDAD LIKE ?;"
      ciudad = 'Madrid'
      cursor.execute(consulta,("%" + ciudad + "%"))
      datos = cursor.fetchall()
      for i in datos:
        print(i)
     
     
   #POR ULTIMO VAMOS A MODIFCAR DATOS DE NUESTRA BBDD --> EN ESTOS CASOS DEBEMOS DE USAR Commit
   
   with conexion.cursor() as cursor:
    consulta = 'UPDATE TABLA_2 set CIUDAD = ? WHERE POBLACION = ?;'
    ciudad = 'México'
    poblacion = 15000000
    cursor.execute(consulta,(ciudad,poblacion))
    
    conexion.commit() --> así nos aseguramos que se han ejecutado los datos de manera correcta.
  
  
  
  
  
  
  
