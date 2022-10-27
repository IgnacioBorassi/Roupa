from urllib import request
from flask import Flask, render_template, request, url_for, redirect
from scraper.scraper import Scraper
from scraper.page_scrapers import Gender

app = Flask(__name__)
@app.route("/",methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        ropa = request.form['ropa']
        lista = Scraper.search(ropa, Gender.MAN.name)
        return render_template('search.html', listas=lista, len=len(lista))

    return render_template('index.html')

@app.route("/search.html",methods = ['POST', 'GET'])
def search():
    lista = []
    if request.method == 'POST':
        ropa = request.form['ropa']
        if ropa != "":
            lista = Scraper.search(ropa, Gender.MAN.name)
        


    return render_template('search.html', listas=lista, len=len(lista))


if __name__ == "__main__":
    app.debug = True
    app.run()