from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
	name: str
	cost: float
	image: str
	link: str