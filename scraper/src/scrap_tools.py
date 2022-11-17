from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time, sys, os, platform


def create_driver():
     script_dir = os.path.dirname(__file__)
     driver = None

     # Depending on the os, the initialization of the driver changes.
     if sys.platform == "win32" or sys.platform == "win64":
          options = Options()
          options.binary_location = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

          driver = webdriver.Firefox(executable_path=f"{script_dir}\\src\\drivers\\geckodriver.exe", options=options)
     elif sys.platform == "linux":
          if platform.freedesktop_os_release()['ID'] == 'linuxmint':
               driver = webdriver.Firefox(executable_path=f'{script_dir}/src/drivers/geckodriver')
          else:
               driver = webdriver.Firefox(executable_path=f'src/drivers/geckodriver')

     assert driver != None, "Driver was not initialized.\n" \
          + f"Maybe the os: {sys.platform}, or the distro: " \
          + f"{platform.freedesktop_os_release()['NAME']} is not supported."

     return driver


def enter_page(driver, url: str):
     driver.get(url)


def wait(seconds):
     time.sleep(seconds)


def scroll(driver, scroll_pause_time: float, scroll_by: int):
     last_height = driver.execute_script("return document.body.scrollHeight")
     new_height = 0

     while True:
          driver.execute_script(f"window.scrollBy(0, {scroll_by});")

          time.sleep(scroll_pause_time)

          new_height += scroll_by
          if new_height >= last_height: break
          last_height = driver.execute_script("return document.body.scrollHeight")


def find_in_find(driver, find_values: tuple, recall) -> list:
     targets = []

     for value in driver.find_elements(find_values[0], find_values[1]):
          targets.append(recall(value))

     return targets
