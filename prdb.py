import mysql.connector
import datetime

def inLogDb(id,query,rv,dt):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="project"
    )

    mycursor = mydb.cursor()
    id=int(id)
    val = (id, query, rv, dt)
    mycursor.execute("INSERT INTO demolog (id, userquery,rvalue,dt_time) VALUES (%s, %s, %s, %s)", val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mydb.close()

def inNLogDb(query,rv,dt):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="sourabh",
      database="minorproject"
    )

    mycursor = mydb.cursor()
    val = (query, rv, dt)
    mycursor.execute("INSERT INTO demonlog (userquery,rvalue,dt_time) VALUES (%s, %s, %s)", val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mydb.close()

def inFLogDb(query,rv,dt):
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="project"
    )

    mycursor = mydb.cursor()
    val = (query, rv, dt)
    mycursor.execute("INSERT INTO demofaillog (userquery,rvalue,dt_time) VALUES (%s, %s, %s)", val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    mydb.close()