from page_scrapers import Gender
from page_scrapers.zara import Zara
from brand import Brand

class Scraper:
	brand_class = {
		Brand.ZARA : Zara
	}

	@staticmethod
	def search(value, gender):
		products = list()

		for brand in Brand:
			if Scraper.brand_class[brand].has_gender(gender):
				if len(Scraper.brand_class[brand].get_genders()) == 1:
					products.extend(Scraper.brand_class[brand].search(value))

				else:
					products.extend(Scraper.brand_class[brand].search(value, gender))

			return products


print(Scraper.search("Camisas", Gender.WOMAN))