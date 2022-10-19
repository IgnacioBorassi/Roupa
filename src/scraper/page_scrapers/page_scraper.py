from page_scrapers import Enum, Gender

class PageScraper:
	gender: dict
	link: dict

	@classmethod
	def has_gender(cls, gender: Gender) -> bool:
		if gender in cls.gender: return True
		