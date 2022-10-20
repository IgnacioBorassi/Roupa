from page_scrapers import Gender
from page_scrapers.zara import Zara
from brand import Brand

class Scraper:
	brand_class = {
		Brand.ZARA : Zara
	}

	@staticmethod
	def search(value, gender):
		for brand in Brand:
			if Scraper.brand_class[brand].has_gender(gender):
				print(Scraper.brand_class[brand].search(value, gender))

print(Scraper.search("Camisas", Gender.WOMAN))