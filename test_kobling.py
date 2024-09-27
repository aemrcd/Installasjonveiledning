
import mysql.connector # pip install mysql-connector-python

mydb = mysql.connector.connect(
host="10.2.4.63",
user="AngelitoDB",
password="Anmea050*",
database="telefonkatalog"
)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM person")
resultater = cursor.fetchall()

for dings in resultater:
    print(dings)