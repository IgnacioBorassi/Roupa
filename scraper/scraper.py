import mariadb
import logging
from datetime import datetime
from src.brands import Zara 
from src.brands import Street47 


class Scraper:
	def __init__(self, conn_parameters):
		self.conn = self.create_connection(conn_parameters)
		self.cursor = self.conn.cursor()
		self.brands = [Zara]


	def create_connection(self, connection_parameters):
		try:
		    conn = mariadb.connect(**connection_parameters)
		except mariadb.Error as e:
		    print(f"Error connecting to MariaDB Platform: {e}")
		    sys.exit(1)

		return conn


	def run(self):
		update_time = datetime.now()

		for brand in self.brands:
			product_categories = brand.run()			
			
			brand_id = self.get_idbrand(brand.get_name())
			
			self.delete_products_by_brand(brand_id)

			for category in product_categories:
				entry_time = datetime.now()

				for product in product_categories[category]:
					args: list = list()

					args.append(brand_id)
					args.append(f"{entry_time}")
					args.append(self.get_idcategory(category))
					args.append(product.gender)
					args.append(product.name)
					args.append(product.cost)
					args.append(product.image)
					args.append(product.link)

					self.cursor.callproc('AddProduct', args)
		
			self.conn.commit()
		
		self.conn.close()
				

	def delete_products_by_brand(self, brand_id: int):
		self.cursor.execute(f"DELETE p, pc FROM products p JOIN products_categories pc WHERE p.id_brand={brand_id}")


	def get_idbrand(self, brand_name: str) -> int:
		self.cursor.execute(f"SELECT id_brand from brands WHERE name='{brand_name}'")

		result = self.cursor.fetchone()
		if result != None:
			return result[0]
		else:
			return result


	def get_idcategory(self, category_name:str) -> int:
		self.cursor.execute(f"SELECT id_category from categories WHERE name='{category_name}'")

		result = self.cursor.fetchone()
		if result != None:
			return result[0]
		else:
			return result
				


if __name__ == "__main__":
	conn_parameters= {
	    "user" : "root",
	    "password" : "",
	    "host" : "0.tcp.sa.ngrok.io",
	    "port" : "",
	    "database" : "roupa_products"
	}

	scraper = Scraper(conn_parameters)
	scraper.run()
