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
   
    return render_template('search.html', listas=lista, len = len(lista))
    
    
    
def listas():
    
    producto = Scraper.search("Camisas", Gender.MAN)
    l = []
    for i in range(0,len(fotos)):
    	
    	l.append([producto[i].image ,producto[i].link, nombre[i], precio[i], logo[i]])
    	
    return l
if __name__ == "__main__":
    app.run()