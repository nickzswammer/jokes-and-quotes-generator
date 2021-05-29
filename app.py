import requests
import json
from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request
from dadjokes import Dadjoke
import mysql.connector
from dotenv import load_dotenv
import os
from flaskext.mysql import MySQL

#Loading Environment Variable for Database Password
load_dotenv()
PASS = os.getenv('PASSWORD')



#create App
app = Flask(__name__)

#Coonnect with Database
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = PASS
app.config['MYSQL_DATABASE_DB'] = 'emailcontact'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

connection = mysql.connect()
cursor = connection.cursor()

#Generate API responses and get values
bill = 'https://belikebill.ga/billgen-API.php?default=1'



#Create Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/jokes')
def jokes():
    return render_template('jokes.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

@app.route('/dadjokes')
def dadjokes():
    dadjokes = Dadjoke()
    joke = dadjokes.joke
    return render_template('dadjokes.html', dadjoke=joke)

@app.route('/billjokes')
def billjokes():
    return render_template('billjokes.html', belikebill=bill)

@app.route('/geekyjokes')
def geekyjokes():
    geeky = requests.get('https://geek-jokes.sameerkumar.website/api?format=json')
    geeky_json = geeky.json()
    geek_joke = geeky_json['joke']
    return render_template('geekyjokes.html', geekjoke=geek_joke)

@app.route('/chucknorris')
def chucknorris():
    chuck = requests.get('https://api.chucknorris.io/jokes/random')
    chuck_json = chuck.json()
    chuck_quote = chuck_json['value']
    return render_template('chucknorris.html', chucknq=chuck_quote)

@app.route('/kanyew')
def kanyew():
    kanye = requests.get('https://api.kanye.rest/')
    kanye_json = kanye.json()
    kanye_quote = kanye_json['quote']
    return render_template('kanyew.html', kanyeq=kanye_quote)

@app.route('/ronswanson')
def ronswanson():
    swanson = requests.get('http://ron-swanson-quotes.herokuapp.com/v2/quotes')
    swanson_json = swanson.json()
    swanson_quote = swanson_json[0]
    return render_template('ronswanson.html', swansonq=swanson_quote)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        insertdatabase = 'INSERT INTO users (name, email, message) VALUES (%s, %s, %s)'
        inputs = (name, email, message)

        cursor.execute(insertdatabase, inputs)
        connection.commit()

        return render_template('contact.html', success_message = "Message sent successfully. I will reach out to you shortly.")

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
