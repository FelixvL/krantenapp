import mysql.connector
import os
def maakverbinding():
    mydb = mysql.connector.connect(
    host="pythondb.mysql.database.azure.com",  #port erbij indien mac
    user="felixadmin",
    password=os.environ.get('ONZEDATABASEWACHTWOORD'),
    database="krantenapp"
    )
    return mydb

def alleartikelen_af():
    mydb = maakverbinding()

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM artikel3")

    myresult = mycursor.fetchall()
    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data

def artikeltoevoegen_af(titel, auteur, categorie):
    mydb = maakverbinding()

    mycursor = mydb.cursor()
    sql = "INSERT INTO artikel3 (titel, auteur, categorie, publiceerdatum) VALUES (%s, %s, %s, CURRENT_TIMESTAMP())"
    val = (titel, auteur, categorie)
    mycursor.execute(sql, val)

    mydb.commit()
    return "opgeslagen"

def artikelmbvid_af(artikelid):
    mydb = maakverbinding()

    mycursor = mydb.cursor()

    sql = ("SELECT * FROM artikel3 WHERE id = "+str(artikelid))
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    keys = [i[0] for i in mycursor.description]

    data = [
        dict(zip(keys, row)) for row in myresult
    ]
    return data

def verwijderartikelmbvid_af(artikelid):
    mydb = maakverbinding()

    mycursor = mydb.cursor()
    sql = "DELETE FROM artikel3 WHERE id = "+str(artikelid)
    mycursor.execute(sql)
    mydb.commit()
    return "deleted"


def heelartikeltoevoegen(gegevens):
    mydb = maakverbinding()

    mycursor = mydb.cursor()
    sql = "INSERT INTO artikel3 (titel, auteur, categorie, publiceerdatum, inhoud, foto) VALUES (%s, %s, %s, CURRENT_TIMESTAMP(), %s, %s)"
    val = (gegevens["titel"], gegevens["auteur"], gegevens["categorie"], gegevens["inhoud"], gegevens["foto"])
    mycursor.execute(sql, val)
    mydb.commit()
    return "{\"inhoud\":\"de post is gelukt\"}"