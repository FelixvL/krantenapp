import mysql.connector
import os

def alleartikelen_af():
    mydb = mysql.connector.connect(
    host="aidatabasedontdelete.mysql.database.azure.com",  #port erbij indien mac
    user="felixadmin",
    password=os.environ.get('ONZEDATABASEWACHTWOORD'),
    database="krantenapp"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM artikel")

    myresult = mycursor.fetchall()
    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data

def artikeltoevoegen_af(titel, auteur, categorie):
    mydb = mysql.connector.connect(
    host="aidatabasedontdelete.mysql.database.azure.com",  #port erbij indien mac
    user="felixadmin",
    password=os.environ.get('ONZEDATABASEWACHTWOORD'),
    database="krantenapp"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO artikel (titel, auteur, categorie) VALUES (%s, %s, %s)"
    val = (titel, auteur, categorie)
    mycursor.execute(sql, val)

    mydb.commit()
    return "opgeslagen"

def artikelmbvid_af(artikelid):
    mydb = mysql.connector.connect(
    host="aidatabasedontdelete.mysql.database.azure.com",  #port erbij indien mac
    user="felixadmin",
    password=os.environ.get('ONZEDATABASEWACHTWOORD'),
    database="krantenapp"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM artikel WHERE id="+artikelid)

    myresult = mycursor.fetchall()
    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data