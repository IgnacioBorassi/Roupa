from enum import Enum, auto
class Gender(Enum):
	WOMAN = auto()
	MAN = auto()

from scrap_tool import ScrapTool as st
from selenium.webdriver.common.by import By
from page_scrapers.page_scraper import PageScraper