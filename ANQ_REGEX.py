# define URL for web.driver
ANQ1 = "https://www.assnat.qc.ca/fr/travaux-parlementaires/commissions/crc-43-1/journal-debats/CRC-230914.html"

# import extensions (Requires : Selenium, BeautifulSoup, Panda)
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
import re

# set options for headless chrome
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# visit web homepage
driver.get(ANQ1)
driver.refresh()
driver.implicitly_wait(10)
page_source = driver.page_source
page_target = driver.find_elements(By.XPATH, '//*[@id="Wrap"]/div[9]/div[3]/div[1]')

############ - Harvest HTML page - UNUSED, Instead set "page_target"
## TASK 1 ## - STATUS : DONE
############

# extract page content and add to a data frame
# a = driver.find_elements(By.XPATH, '//*[@id="Wrap"]/div[9]/div[3]/div[1]')
#     for element in a:
#        print(element.text)
        
# a_list = [element.get_attribute('outerHTML') for element in a]
#     for element in a_list:
#        print(element.text)

# create data frame
#df1 = pd.DataFrame(list(zip(a_list)),
#               columns =['page'])

# print the data frame
# print(df1)
# df1.to_csv('ANQ_REGEX_1.csv', index=False)

############ - Extract target content
## TASK 2 ## - STATUS : TO DO
############

# Set empty containers
extracted_text_list = []

# Set Page Source for BeautifulSoup html parser - TypeError: expected string or bytes-like object, got 'list'
soup = BeautifulSoup(page_target, "html.parser")

# Find all <b> tags within the page HTML
bold_tags = soup.find_all("b")

# Extract text within each <b> tag and print it
for bold_tag in bold_tags:
    bold_text = bold_tag.get_text()
#    print("Text within <b> tag:", bold_text)

# Extract text within each <b> tag and add to a list
bold_text_list = [bold_tag.get_text() for bold_tag in bold_tags]

# Set RegEx patterns
text_extract_core = r'</b>(.*?)<b>'
# OLD - text_marker_substract = r'(<[A-Za-z]+>|</[A-Za-z]+>)'
# OLD - speaker_tags_substract = r'(<[A-Za-z]+>|</[A-Za-z]+>)'
# OLD - pattern = r'\[.*?\]'

# Use re.findall to extract text between <b> tags - TypeError: expected string or bytes-like object, got 'list'
content = re.findall(text_extract_core, target, re.DOTALL)

# Print the extracted text
for match in content:
  extracted_text_list.append(match)
    # print("Text between </b> and <b> tags:", match)

############ - Create a table : speakers, texts, percentages (y/n?)
## TASK 3 ## - STATUS : TO DO
############

# Add speakers to data frame
df2 = pd.DataFrame({'Speakers': bold_text_list})

# Print speaker data frame
# print(df2)
# df2.to_csv('ANQ_REGEX_2.csv', index=False)

# Add texts to data frame
df3 = pd.DataFrame({'Text': extracted_text_list})
df3.drop(df3.index[0:4], inplace=True)

# Print text data frame
# print(df3)
# df3.to_csv('ANQ_REGEX_3.csv', index=False)

# Combine speaker and text data frames
df4 = pd.concat([df2, df3], axis=1)
# print(df4)

# Check for '%' in all cells and return True or False in a new column
df4['Pourcentages'] = df4.apply(lambda row: row.astype(str).str.contains('%').any(), axis=1)

# Extract '%' in another column
df4['Chiffres du pourcentage'] = df4['Text'].str.extractall(r'(\d\d\s+%|\d,\d\s+%|\d\d%|\d,\d%|\d\s+%|\d%)').groupby(level=0).agg(', '.join)

# Save complete data frame
df4.to_csv('ANQ_REGEX_4.csv', index=False)

############ - Clean data : 1) remove dates, 2) texts together 3) uniform names
## TASK 4 ## - STATUS : TO DO
############

# Remove "(...)" content in speaker data frame
df4['Speakers'] = df4['Speakers'].str.replace(r'(\s+\([^)]*\)\s+)', '', regex=True)

# Remove "[""]" content in speaker data frame
df4['Speakers'] = df4['Speakers'].str.replace(r'("\s+)', '', regex=True)

# Remove ":" content in speaker data frame
df4['Speakers'] = df4['Speakers'].str.replace(r'(:|\s+:)', '', regex=True)

# Remove "<...>" containers in data frame
df4['Text'] = df4['Text'].str.replace(r'(<[A-Za-z]+>|</[A-Za-z]+>)', '', regex=True)

# Remove unwanted data "• () •" in data frame 
df4['Text'] = df4['Text'].str.replace(r'(•\s+\([^)]*\)\s+•|\([^)]*\))', '', regex=True)

# Remove unwanted data "<.*>" in data frame
df4['Text'] = df4['Text'].str.replace(r'(<.*>)', '', regex=True)

# Remove unwanted data "&nbsp, Haut de la page" in data frame
df4['Text'] = df4['Text'].str.replace(r'(&nbsp;|Haut de la page)', '', regex=True)

# Remove unwanted data "Date" in data frame
df4['Text'] = df4['Text'].str.replace(r'(\d\d\s+h\s+\d\d|\d\d\s+h)', '', regex=True)

df4.to_csv('ANQ_REGEX_CLEAN.csv', index=False)

# closing the driver
driver.quit()
