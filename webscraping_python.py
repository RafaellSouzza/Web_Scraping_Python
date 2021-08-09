
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import json

url = "https://g1.globo.com/politica/"

# chrome_options=chrome_options
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)
driver.implicitly_wait(10)

element = driver.find_element_by_class_name("_l")
html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')

for materia in soup.find_all("div", attrs={"class": "_b"}):
    print(materia)
    print("\n\n")


driver.quit()
