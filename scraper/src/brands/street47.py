from src.brand import Brand
from src.product import Product
from src.scrap_tools import * 
from typing import List
from selenium.webdriver.support.wait import WebDriverWait 
import selenium.webdriver.support.expected_conditions as EC


class Street47(Brand):
	name = "47Street"
	link = {
		"search_by_id" : lambda id : f"https://www.47street.com.ar/{id}?map=productClusterIds"
	}
	categories = {
		'Remeras': 267, 'Buzos': 172, 'Camperas': 252, 
		'Tops': 271, 'Bodies': 171, 'Bañadores': 172,
		'Musculosas': 278, 'Shorts': 279, 'Calzas': 277,
		'Faldas': 272, 'Babuchas': 268, 'Pantalones': 269,
		'Jeans': 270, 'Vestidos': 273, 'Sweaters': 274,
		'Camisas': 275, 'Enteros': 276, 'Denims': 281,
		'Blazers': 173, 'Zapatillas': 189, 'Sandalias': 188,
		'Botas': 190
		}
	genders = ['WOMAN']


	@classmethod
	def _search(cls, id):
		driver = create_driver()
		driver.maximize_window()

		enter_page(driver, cls.link['search_by_id'](id))
		scroll(driver, 1, 300)
		WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'om-popup-close-x'))).click()

		products = find_in_find(
			driver,
			(By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem'),
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
				'WOMAN'
				)
			for product in products
		]


	@classmethod
	def _search_recall(cls, value):
		data = dict()
		
		data["link"] = value.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-clearLink').get_attribute('href')
		data["image"] = value.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-imageNormal').get_attribute('src')
		data["name"] = value.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-productBrand').text

		cost_container = value.find_element(By.CLASS_NAME, 'vtex-product-price-1-x-sellingPriceValue')
		cost = [i.text for i in cost_container.find_elements(By.CLASS_NAME, 'vtex-product-price-1-x-currencyInteger')]
		data["cost"] = ''.join(cost)
		
		return data


	@classmethod
	def run(cls, categories: List[str] = list()) -> dict:
		if not categories: categories = cls.categories

		products: dict = dict()
		
		for category in categories:
			products[category] = list()
			products[category].extend(cls._search(cls.categories[category]))	

		return products
