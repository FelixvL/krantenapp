from flask import Flask
from flask import request
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
    return "<p>Hello, Groningen! Of ik bedoel friesland Extra</p>"

@app.route("/tweede/<artikeltitel>")
def tweede(artikeltitel):
    mydb = mysql.connector.connect(
    host="pythondb.mysql.database.azure.com",  #port erbij indien mac
    user="felixadmin",
    password=os.environ.get('ONZEDATABASEWACHTWOORD'),
    database="krantenapp"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM artikel3")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    sql = "INSERT INTO artikel3 (titel, auteur) VALUES (%s, %s)"
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

@app.route("/artikelmbvid/<artikelid>")
def artikelmbvid(artikelid):
    return allefuncties.artikelmbvid_af(int(artikelid))

@app.route("/verwijderartikelmbvid/<artikelid>")
def verwijderartikelmbvid(artikelid):
    return allefuncties.verwijderartikelmbvid_af(int(artikelid))


@app.route("/heelartikeltoevoegen", methods = ['GET','POST'])
def heelartikeltoevoegen():
    if request.method == 'POST':
        return allefuncties.heelartikeltoevoegen(request.json)
    else: 
        return "{\"info\":\"Dit was geen post\"}"
