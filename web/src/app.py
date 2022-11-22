from urllib import request
from flask import Flask, render_template, request, url_for, redirect

import mariadb
import sys

class ListaProductos:
    def __init__(self):
        self.lista=[]

    def set_lista(self, listaNueva):
        self.lista = listaNueva
        
    def get_lista(self):
        
        return self.lista


conn_params= {
    "user" : "root",
    "password" : "pX5jxpups2TWnx",
    "host" : "0.tcp.sa.ngrok.io",
    "port" : 16792,
    "database" : "roupa_products"
}

def get_roupa(ropa, genero):
    lista = []
    
    try:
        conn = mariadb.connect(**conn_params)
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    cursor = conn.cursor()
    try:
        if ropa != "" and genero != "todo":
            statement = "SELECT a.name, a.cost, a.image, a.link, a.gender, b.icon FROM products a, brands b WHERE a.id_brand = b.id_brand AND a.name LIKE '%"
            statement += ropa
            statement += "%'"
            statement += "AND a.gender='"
            statement += genero 
            statement += "' ORDER BY a.cost;"
            data = (ropa,)
            
            cursor.execute(statement, data)
            for (ropa) in cursor:
                lista.append(ropa)
            return lista
        if ropa == "" and genero != "todo":
            statement = "SELECT a.name, a.cost, a.image, a.link, a.gender, b.icon FROM products a, brands b WHERE a.id_brand = b.id_brand AND a.gender='"
            statement += genero
            statement += "' ORDER BY a.cost"
            data = (ropa,)
            cursor.execute(statement,data)
            for (ropa) in cursor:
                lista.append(ropa)
            cursor.close()
            return lista
        if ropa != "" and genero == "todo":
            statement = "SELECT a.name, a.cost, a.image, a.link, a.gender, b.icon FROM products a, brands b WHERE a.id_brand = b.id_brand AND a.name LIKE '%"
            statement += ropa
            statement += "%'"
            statement += " ORDER BY a.cost"
            data = (ropa,)
            cursor.execute(statement,data)
            for (ropa) in cursor:
                lista.append(ropa)
            cursor.close()
            return lista
        statement = "SELECT a.name, a.cost, a.image, a.link, a.gender, b.icon FROM products a, brands b WHERE a.id_brand = b.id_brand"
        statement += " ORDER BY a.cost"
        data = (ropa,)
        cursor.execute(statement,data)
        for (ropa) in cursor:
            lista.append(ropa)

        cursor.close()
        return lista
        
        
    except mariadb.Error as e:
      print(f"Error retrieving entry from database: {e}")

listaproducto = ListaProductos()

app = Flask(__name__)
@app.route("/",methods = ['POST', 'GET'])
def home():
    lista = []
    if request.method == 'POST':
        ropa = request.form['ropa']
        lista = get_roupa(ropa, "todo")
        listaproducto.set_lista(lista)
        
        if lista == None:
            lista=[]
        return render_template('search.html', listas=lista, len=len(lista))

    return render_template('index.html')

@app.route("/search",methods = ['POST', 'GET'])
def search():
    lista = []
    
    if request.method == 'POST':
        
        ropa = request.form['ropa'] 
        genero = request.args.get("genero", "todo")
        lista = get_roupa(ropa, genero)
        listaproducto.set_lista(lista)
        return render_template('search.html', listas=lista, len=len(lista))

    else:
        
        lista = listaproducto.get_lista()
        
        genero = request.args.get("genero", "todo")
        listagen =[]
        if genero == "todo":
            return render_template('search.html', listas=lista, len=len(lista))
        else:
            for i in range(1, len(lista)):
                if lista[i][4] == genero:
                    listagen.append(lista[i])
        
        return render_template('search.html', listas=listagen, len=len(listagen))
        

    
    if lista == None:
        lista=[]
        
    return render_template('search.html', listas=lista, len=len(lista))



if __name__ == "__main__":
    app.debug = True
    app.run()