import mysql.connector


## Connect to server
connexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password = 'password123'
)

## Get a cursor
cursor = connexion.cursor()

##Excute a query
cursor.execute("Create DataBase my_database")
print("All Done !")