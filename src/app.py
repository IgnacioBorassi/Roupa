from flask import Flask, render_template


app = Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')
   

    
@app.route("/search.html")
def search():
    
    lista = listas()
    print(lista)
    return render_template('search.html', listas=lista, len = len(lista))
    
    
    
def listas():
    links = ["https://articulo.mercadolibre.com.ar/MLA-1147314066-remeras-algodon-peinado-241-lisas-ninos-fabricantes-_JM?searchVariation=174838699114#searchVariation=174838699114&position=3&search_layout=grid&type=item&tracking_id=70f66413-13db-48da-91df-8aa00695beee", "https://www.zara.com/ar/es/camisa-rayas-algodon---lino-p03929370.html?v1=192033739", "https://www.zara.com/ar/es/camisa-rayas-algodon---lino-p03929374.html?v1=192033730","https://www.zara.com/ar/es/camisa-popelin-elastico-p04395471.html?v1=189298402","https://www.zara.com/ar/es/camisa-pana-p07545580.html?v1=177606395"]
    fotos = ["https://http2.mlstatic.com/D_NQ_NP_2X_999782-MLA50771896245_072022-F.webp","https://static.zara.net/photos///2022/S/0/2/p/3929/370/710/2/w/750/3929370710_6_1_1.jpg?ts=1665998674874","https://static.zara.net/photos///2022/S/0/2/p/3929/374/400/2/w/707/3929374400_6_1_1.jpg?ts=1665998673623","https://static.zara.net/photos///2022/S/0/2/p/4395/471/800/502/w/750/4395471800_2_1_1.jpg?ts=1655390632671","https://static.zara.net/photos///2022/S/0/2/p/7545/580/634/2/w/750/7545580634_2_1_1.jpg?ts=1655396622640"]
    nombre=["Remeras Algodón Peinado", "CAMISA RAYAS ALGODÓN - LINO", "CAMISA RAYAS ALGODÓN - LINO", "CAMISA POPELÍN ELÁSTICO","CAMISA PANA"]
    precio=["1.230", "15.990", "15.990", "15.990","15.990"]
    logo = ["https://logodownload.org/wp-content/uploads/2018/10/mercado-libre-logo.png","https://img2.freepng.es/20180704/jrk/kisspng-zara-logo-inditex-brand-lacoste-logo-5b3d343e83de54.0243255115307377265401.jpg", "https://img2.freepng.es/20180704/jrk/kisspng-zara-logo-inditex-brand-lacoste-logo-5b3d343e83de54.0243255115307377265401.jpg","https://img2.freepng.es/20180704/jrk/kisspng-zara-logo-inditex-brand-lacoste-logo-5b3d343e83de54.0243255115307377265401.jpg","https://img2.freepng.es/20180704/jrk/kisspng-zara-logo-inditex-brand-lacoste-logo-5b3d343e83de54.0243255115307377265401.jpg","https://img2.freepng.es/20180704/jrk/kisspng-zara-logo-inditex-brand-lacoste-logo-5b3d343e83de54.0243255115307377265401.jpg"]
    producto = []
    
    for i in range(0,len(fotos)):
    	
    	producto.append([fotos[i],links[i], nombre[i], precio[i], logo[i]])
    	
    
    return producto
if __name__ == "__main__":
    app.run()