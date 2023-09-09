# THIS LINE WAS ADDED ON SEPTEMBER 8th 2023

# Experiments to scrape websites with python and selenium
# Guide 1 : https://www.geeksforgeeks.org/get-all-text-of-the-page-using-selenium-in-python/
# Guide 2 : https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a
# Also a lot of Stack Overflow

# Website scraped http://books.toscrape.com/index.html

# define URL's
toscrape = "http://books.toscrape.com/index.html"
scrapethissite = "https://www.scrapethissite.com/pages/simple/"

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
driver.get(scrapethissite)
driver.implicitly_wait(10)

# print elements available through Selenium commands - anything with a hashtag after this is an individual successful attempt
# print(driver.find_element(By.XPATH, "/html/body/div/section/div").text)

country_name_list = []
country_name = driver.find_elements(By.CLASS_NAME, "country-name")
for e in country_name:
    print(e.text)

df = pd.DataFrame(country_name,columns=['country name'])
df.to_csv('country_name.csv', index=False)
driver.quit()
