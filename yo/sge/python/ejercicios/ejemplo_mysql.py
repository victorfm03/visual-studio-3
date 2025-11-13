import pymysql

connection = pymysql.connect(
    host="db",      # IP del host Docker
    user="root",
    password="test",
    database="libreria",
    port=3306
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM libro")

for row in cursor:
    print(row)

cursor.execute("SELECT * FROM genero")

rows = cursor.fetchall()

connection.close() # cerramos la conexión si no vamos a trabajar más con la bbdd

for row in rows:
    print('idgenero:', row[0], 'genero:', row[1])

