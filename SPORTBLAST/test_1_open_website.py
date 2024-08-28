import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_1_open_website():

    options = Options()
    options.headless = False

    driver = webdriver.Chrome(service = chrome_service(ChromeDriverManager().install()), options=options)

    driver.get("https://sportblast.pl")

    #time.sleep(1)

    WebDriverWait(driver, 10).until(EC.title_contains("SPORT BLAST - Hantle żeliwne, obciążenie, sztangi, gryfy"))

    #time.sleep(1)

    driver.quit()

