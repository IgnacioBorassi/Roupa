from flask import Flask, render_template
from scraper.scraper import Scraper
from scraper.page_scrapers import Gender

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search.html")
def search():
    lista = Scraper.search("Camisas", Gender.MAN)
    return render_template('search.html', listas=lista, len=len(lista))
if __name__ == "__main__":
    app.run()