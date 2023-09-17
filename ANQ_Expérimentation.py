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
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# visit web homepage
driver.get(ANQ)
driver.refresh()
driver.implicitly_wait(10)

# identifying the number of rows having <tr> tag
# rows = []
# rows = driver.find_elements(By.XPATH, '//*[@id="tblListeJournal"]/tbody/tr')
# print(len(rows))

# Extracting the length of table :
table_all = len(driver.find_elements(By.XPATH,'//*[@id="tblListeJournal"]/tbody/tr'))
print(table_all)

# creating empty list to save data:
final_list = []
date = []
assemblee =[]
session = []
version =[]
mandats = []

# for extracting date
for i in range(table_all+1):
    d = driver.find_elements(By.XPATH, 
        '//*[@id="tblListeJournal"]/tbody/tr[' + 
        str(i) + ']/td[1]/a')
    for element in d:
        date.append(element.text)

# for extracting assemblee
for i in range(table_all+1):
    a = driver.find_elements(By.XPATH, 
        '//*[@id="tblListeJournal"]/tbody/tr[' + 
        str(i) + ']/td[2]')
    for element in a:
        assemblee.append(element.text)

# for extracting which session
for i in range(table_all+1):
    s = driver.find_elements(By.XPATH, 
        '//*[@id="tblListeJournal"]/tbody/tr[' + 
        str(i) + ']/td[3]')
    for element in s:
        session.append(element.text)
        
# for extracting which version
for i in range(table_all+1):
    v = driver.find_elements(By.XPATH, 
        '//*[@id="tblListeJournal"]/tbody/tr[' + 
        str(i) + ']/td[4]')
    for element in v:
        version.append(element.text)      

# for extracting which mandats
for i in range(table_all+1):
    m = driver.find_elements(By.XPATH, 
        '//*[@id="tblListeJournal"]/tbody/tr[' + 
        str(i) + ']/td[5]')
    for element in m:
        mandats.append(element.text)

df=pd.DataFrame(list(zip(date,assemblee,session,version,mandats)),
               columns =['Date', 'Assemblee', 'Session','Version','Mandats'])

print(df)
df.to_csv('list.csv')
driver.quit()

# FIND ELEMENTS OPTIONS (TEST 1)
# href = driver.find_elements(By.ID, "tblListeJournal")
# href = driver.find_elements(By.NAME, "a")
# href = driver.find_elements(By.XPATH, "//a[@href]")
# href = driver.find_elements(By.LINK_TEXT, "a")
# href = driver.find_elements(By.PARTIAL_LINK_TEXT, "20")
# href = driver.find_elements(By.TAG_NAME, "a")
# href = driver.find_elements(By.CLASS_NAME, "a")
# href = driver.find_elements(By.CSS_SELECTOR, "a")
# for elem in href:
#    print(elem.get_attribute("href"))
