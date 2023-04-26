import getpass
import oracledb
import os

connection = oracledb.connect(
    user="ADMIN",
    password="Holaolaola2021=-",
    config_dir = "polls\db", #solo nos recupera el path local
    dsn=r"(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.sa-santiago-1.oraclecloud.com))(connect_data=(service_name=g3e61719689d692_of9irekmrz0t3e0r_low.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))",
    wallet_location= "polls\db",
    wallet_password= "Holaolaola2021=-") #si le habian puesto la clave
print(f"{46*'-'}\n Conectado a la base de datos Oracle Database \n{46*'-'}")

# variables
counter = 0
lista = []
lista2 = []
lista3 = []
querys = []

with connection.cursor() as cursor:
    d = cursor.execute("""
            SELECT *
            FROM prueba""")
    counter += 1
    for row in cursor:
        #print(row[0],"-",row[1])
        lista.append(row)       
    querys.append(lista)

with connection.cursor() as cursor:
    d = cursor.execute("""
            SELECT *
            FROM prueba WHERE id < 3""")
    counter += 1
    for row in cursor:
        #print(row[0],"-",row[1])
        lista2.append(row)       
    querys.append(lista2)

with connection.cursor() as cursor:
    d = cursor.execute("""
            SELECT table_name
            FROM user_tables""")
    counter += 1
    for row in cursor:
        #print(row[0],"-",row[1])
        lista3.append(row)       
    querys.append(lista3)

print(f"\nRetirando {counter} querys:")
for arr in querys:
    print(f"Data: {arr}")
print("")