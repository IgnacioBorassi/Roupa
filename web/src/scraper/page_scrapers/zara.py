from scraper.product import Product
from scraper.page_scrapers import st, By, Enum, Gender, PageScraper, Brand

class Zara(PageScraper):
	gender = {Gender.MAN.name : 'MAN', Gender.WOMAN.name : 'WOMAN'}
	link = {
		"search" : lambda product_name, gender : f"https://www.zara.com/ar/es/search?searchTerm={product_name}&section={gender}"
	}

	@staticmethod
	def search(product_name, gender):
		driver = st.create_driver()
		st.enter_page(driver, Zara.link["search"](product_name, gender))
		st.scroll(driver, 1, 300)
		values = st.find_in_find(
			driver,
			(By.CLASS_NAME, 'product-grid-product'),
			Zara._search_recall
		)
		driver.close()

		return values


	@staticmethod
	def _search_recall(value) -> Product:
		link = value.find_element(By.CLASS_NAME, 'product-link').get_attribute('href') 
		img_tag = value.find_element(By.CLASS_NAME, 'media-image__image')
		name = img_tag.get_attribute('alt')
		img = img_tag.get_attribute('src')

		cost = value.find_element(By.CLASS_NAME, 'money-amount__main').text
		# Convierte el texto del cost (ej: '23.990,00 ARS') en un float (ej: 23990.00)
		cost = float(cost[0:len(cost)-3].replace('.', '').replace(',', '.')) 
		
		return Product(Brand.ZARA, name, cost, img, link)
