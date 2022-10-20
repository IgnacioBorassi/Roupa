from page_scrapers import Gender

class PageScraper:
	gender: dict
	link: dict

	@classmethod
	def get_genders(cls):
		return cls.gender


	@classmethod
	def has_gender(cls, gender: Gender) -> bool:
		if gender in cls.gender: return True
		