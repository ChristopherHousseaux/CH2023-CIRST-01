# define URL's
ANQ = "https://www.assnat.qc.ca/fr/travaux-parlementaires/journaux-debats.html"

# import required elements and extensions
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

# set options for headless chrome
options = Options()
# options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# visit web homepage
driver.get(ANQ)
driver.refresh()
driver.implicitly_wait(10)

# find button element
button = driver.find_elements(By.XPATH, '//*[@id="ctl00_ColCentre_ContenuColonneGauche_PaginationBas_lkbPageSuivante"]')

# click the button
driver.execute_script("arguments[0].click();", button);
print("Page title is: ")
print(driver.title)

# driver.quit()
