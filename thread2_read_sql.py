import mysql.connector
def request_sql_table1():
  mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="solar_database"
  )

  mycursor = mydb.cursor()
  mycursor.execute("SELECT name,address FROM buffer_table")
  myresult = mycursor.fetchall()
  if(len(myresult)>0):
    return myresult
  else:
    return myresult
def request_sql_table2():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="solar_database"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ID,TIME_START,TIME_STOP FROM issue_table")
    myresult = mycursor.fetchall()
    if(len(myresult)>0):
      return myresult
    
