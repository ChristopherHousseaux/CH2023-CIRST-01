# TÂCHES
# 1. DONE - Récupérer le html de la page suivante : https://www.assnat.qc.ca/fr/travaux-parlementaires/commissions/crc-43-1/journal-debats/CRC-230914.html
# 2. extraire toutes les interventions
# 3. Nettoyer et reconstruire les interventions dans un tableau à trois colonnes (intervenant(e)s, interventions et Présence/Absence de mobilisation de pourcentage) 
# 4. nettoyer les données :
# 4.1. Retirer les indications temporelles (e.g. • (11 h 40) •)
# 4.2. Les interventions sont complètes, cest-à-dire quune intervention séparé en plusieurs balises est reconstruite en une seule tout en gardant la mise en forme (des sauts de lignes sont ajoutés en remplacement) 
# 4.3. Le nom des interventant(e)s est uniformisé (Mr. ou Mme. NOMDEFAMILLE)


# define URL's
ANQ1 = "https://www.assnat.qc.ca/fr/travaux-parlementaires/commissions/crc-43-1/journal-debats/CRC-230914.html"

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
driver.get(ANQ1)
driver.refresh()
driver.implicitly_wait(10)

print(driver.find_element(By.XPATH, '//*[@id="Wrap"]/div[9]/div[3]/div[1]').text)
 
# Closing the driver
driver.quit()
