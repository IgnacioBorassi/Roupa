import math
from scraper.product import Product
from scraper.page_scrapers import st, By, Enum, Gender, PageScraper, Brand
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Equus(PageScraper):
	gender = {Gender.MAN.name : 'MAN'}
	link = {
		'search' : lambda product_name, index=1: f'https://www.equus.com.ar/{product_name}?_q=&map=ft&page={index}',
	}

	@staticmethod
	def search(product_name):
		driver = st.create_driver()

		st.enter_page(driver, Equus.link['search'](product_name))
		st.wait(6)
		products_quantity = driver.find_element(
			By.CLASS_NAME, 'vtex-search-result-3-x-totalProducts--layout'
			).find_element(By.TAG_NAME, 'span').text
		products_quantity = int(products_quantity.replace(' Productos', ''))
		products = []
		for i in range(2, math.ceil(products_quantity/12), 1):
			for j in range(3):
				driver.execute_script(f"window.scrollBy(0, 500);")
			st.wait(6)

			products.extend(
				st.find_in_find(
					driver,
					(By.CLASS_NAME, 'vtex-search-result-3-x-galleryItem--normal'),
					Equus._search_recall
			))

			st.enter_page(driver, Equus.link['search'](product_name, i))
			st.wait(6)
			

		driver.close()
		return products
	

	@staticmethod
	def _search_recall(value) -> Product:

		name = value.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-productNameContainer').text

		cost_tag = value.find_element(By.CLASS_NAME, 'vtex-store-components-3-x-sellingPrice')
		cost = ""
		for j in cost_tag.find_elements(By.CLASS_NAME, 'vtex-product-summary-2-x-currencyInteger'):
			cost += j.text
		cost = float(cost)

		image = value.find_element(By.CLASS_NAME, 'vtex-product-summary-2-x-mainImageHovered').get_attribute('src')	
		link = value.find_element(By.TAG_NAME, 'a').get_attribute('href')
		
		
		return Product(Brand.EQUUS, name, cost, image, link)
