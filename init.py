import mysql.connector


def con ():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="liloo.kitbusca"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM accounts")
    myresult = mycursor.fetchall()

    for x in myresult:
        return (x)


print(con())