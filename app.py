from flask import Flask
import mysql.connector
import os
from dotenv import load_dotenv
from flask_cors import CORS, cross_origin

import allefuncties

load_dotenv()
app = Flask(__name__)

cors = CORS(app)

# je mag nooit 2 dezelfde routes hebben of 2 dezelfde methode namen
@app.route("/")
def hello_world():
    return "<p>Hello, Groningen!</p>"

@app.route("/tweede/<artikeltitel>")
def tweede(artikeltitel):
    mydb = mysql.connector.connect(
    host="pythondb.mysql.database.azure.com",  #port erbij indien mac
    user="felixadmin",
    password=os.environ.get('ONZEDATABASEWACHTWOORD'),
    database="krantenapp"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM artikel")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    sql = "INSERT INTO artikel (titel, auteur) VALUES (%s, %s)"
    val = (artikeltitel, "harry mulish")
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    return "<p>Wat is die route eigenlijk</p>"

@app.route("/uitrekenen/<getal1>/<getal2>")
def uitrekenen(getal1, getal2):
    totaal = int(getal1) + int(getal2)
    return "<p>het totaal is: "+str(totaal)+"</p>"

@app.route("/favorietestad/<stad>")
def favorietestad(stad):
    return "<p>Mijn favoriete stad is: "+stad+"</p>"

@app.route("/alleartikelen/")
def alleartikelen():
    return allefuncties.alleartikelen_af()

@app.route("/artikeltoevoegen/<titel>/<auteur>/<categorie>")
def artikeltoevoegen(titel, auteur, categorie):
    return allefuncties.artikeltoevoegen_af(titel, auteur, categorie)
