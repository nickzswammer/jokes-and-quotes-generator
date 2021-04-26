import requests
import json
from flask import Blueprint, render_template
from flask import Flask, redirect, url_for, render_template, request
from dadjokes import Dadjoke


#create App
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
