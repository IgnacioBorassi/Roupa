from urllib import request
from flask import Flask, render_template, request, url_for, redirect

import mariadb
import sys



conn_params= {
    "user" : "root",
    "password" : "pX5jxpups2TWnx",
    "host" : "0.tcp.sa.ngrok.io",
    "port" : 19600,
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
            statement = "SELECT name, cost, image, link, id_brand, gender FROM products WHERE name LIKE '%"
            statement += ropa
            statement += "%'"
            statement += "AND gender='"
            statement += genero 
            statement += "' ORDER BY cost;"
            data = (ropa,)
            
            cursor.execute(statement, data)
            for (ropa) in cursor:
                lista.append(ropa)
            return lista
        if ropa == "" and genero != "todo":
            statement = "SELECT name, cost, image, link, id_brand , gender FROM products WHERE gender='"
            statement += genero
            statement += "' ORDER BY cost"
            data = (ropa,)
            cursor.execute(statement,data)
            for (ropa) in cursor:
                lista.append(ropa)
            cursor.close()
            return lista
        if ropa != "" and genero == "todo":
            statement = "SELECT name, cost, image, link, id_brand , gender FROM products WHERE name LIKE '%"
            statement += ropa
            statement += "%'"
            statement += " ORDER BY cost"
            data = (ropa,)
            cursor.execute(statement,data)
            for (ropa) in cursor:
                lista.append(ropa)
            cursor.close()
            return lista
        statement = "SELECT name, cost, image, link, id_brand FROM products"
        statement += " ORDER BY cost"
        data = (ropa,)
        cursor.execute(statement,data)
        for (ropa) in cursor:
            lista.append(ropa)

        cursor.close()
        return lista
        
        
    except mariadb.Error as e:
      print(f"Error retrieving entry from database: {e}")



app = Flask(__name__)
@app.route("/",methods = ['POST', 'GET'])
def home():
    lista = []
    if request.method == 'POST':
        ropa = request.form['ropa']
        lista = get_roupa(ropa, "todo")
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
        print(genero)
        print(ropa)
        lista = get_roupa(ropa, genero)
    
        return render_template('search.html', listas=lista, len=len(lista))

    else:
        genero = request.args.get("genero", "todo")
        

    
    if lista == None:
        lista=[]
        
    return render_template('search.html', listas=lista, len=len(lista))



if __name__ == "__main__":
    app.debug = True
    app.run()