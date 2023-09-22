# define URL's
ANQ = "https://www.assnat.qc.ca/fr/travaux-parlementaires/journaux-debats.html"

# import required elements and extensions
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

# set options for headless chrome
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# visit web homepage
driver.get(ANQ)
driver.refresh()
driver.implicitly_wait(10)

# Extracting the length of table :
table_all = len(driver.find_elements(By.XPATH,'//*[@id="tblListeJournal"]/tbody/tr'))
print(table_all)

# Define values
l = []
link = []

# Find the element with the link
for i in range(table_all+1):
  l = driver.find_elements(By.XPATH, '//*[@id="tblListeJournal"]/tbody/tr[' + str(i) + ']/td[1]/a')
  for element in l:
    link.append(element.text)

print(l.get_attribute('href'))

df=pd.DataFrame(list(zip(link)),
               columns =['Lien'])

print(df)
df.to_csv('links.csv')
driver.quit()

# Extract the link from the element
# link = link_element.get_attribute("href")

# Verify the link
# print(link)
