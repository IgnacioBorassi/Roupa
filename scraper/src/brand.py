from typing import List


class Brand():
	name: str = str()
	categories: List[str] = list() 

	@classmethod
	def get_name(cls) -> str:
		return cls.name


	@classmethod
	def get_categories(cls) -> List[str]:
		return cls.categories