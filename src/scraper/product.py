from dataclasses import dataclass
from scraper.brand import Brand

@dataclass(frozen=True)
class Product:
	brand: Brand
	name: str
	cost: float
	image: str
	link: str