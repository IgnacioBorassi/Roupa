from src.brand import Brand
from src.product import Product
from src.scrap_tools import * 
from typing import List


class Zara(Brand):
	name = "Zara"
	link = {
		'search' : lambda product_name, gender : f"https://www.zara.com/ar/es/search?searchTerm={product_name}&section={gender}"
	}
	categories = ['Blazers', 'Trajes', 'Camisas', 'Camisetas', 'Buzos', 'Pantalones', 'Jeans', 'Bermudas', 'Zapatos']
	genders = ['MAN', 'WOMAN']


	@classmethod
	def _search(cls, product_name, gender):
		driver = create_driver()
		driver.maximize_window()

		enter_page(driver, cls.link['search'](product_name, gender))
		scroll(driver, 1, 300)
		products = find_in_find(
			driver,
			(By.CLASS_NAME, 'product-grid-product'),
			cls._search_recall
		)
		driver.close()

		return [
			Product(
				product['name'],
				cls.get_name(), 
				product['cost'],
				product['image'],
				product['link'],
				gender
				)
			for product in products
		]


	@classmethod
	def _search_recall(cls, value):
		data = dict()
		data["link"] = value.find_element(By.CLASS_NAME, 'product-link').get_attribute('href') 
		img_tag = value.find_element(By.CLASS_NAME, 'media-image__image')
		data["name"] = img_tag.get_attribute('alt')
		data["image"] = img_tag.get_attribute('src')

		cost = value.find_element(By.CLASS_NAME, 'money-amount__main').text
		# Convierte el texto del cost (ej: '23.990,00 ARS') en un float (ej: 23990.00)
		data["cost"] = float(cost[0:len(cost)-3].replace('.', '').replace(',', '.')) 
		
		return data


	@classmethod
	def run(cls, categories: List[str] = list()) -> dict:
		if not categories: categories = cls.categories

		products: dict = dict()
		
		for category in categories:
			products[category] = list()
			for gender in cls.genders:
				products[category].extend(cls._search(category, gender))


		return products