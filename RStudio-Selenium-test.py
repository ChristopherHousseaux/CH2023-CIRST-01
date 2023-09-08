# THIS LINE WAS ADDED ON SEPTEMBER 8th 2023

# Experiments to scrape websites with python and selenium
# Guide 1 : https://www.geeksforgeeks.org/get-all-text-of-the-page-using-selenium-in-python/
# Guide 2 : https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a
# Also a lot of Stack Overflow

# Website scraped http://books.toscrape.com/index.html

# define toscrape URL
toscrape = "http://books.toscrape.com/index.html"

# import required elements and extensions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# set options for headless chrome
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# visit web homepage
driver.get(toscrape)
time.sleep(5)

# print elements available through Selenium commands - anything with a hashtag after this is an individual successful attempt

# print(driver.find_element(By.XPATH, "/html/body").text)

# print(driver.find_element(By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol/li[2]").text)

print(driver.find_element(By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol").text)

# print(driver.title)

# print(driver.current_url)

driver.quit()