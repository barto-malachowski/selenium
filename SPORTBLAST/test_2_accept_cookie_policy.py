import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_2_accept_cookie_policy():

    options = Options()
    options.headless = False

    driver = webdriver.Chrome(service = chrome_service(ChromeDriverManager().install()), options=options)

    #Open the website
    driver.get("https://sportblast.pl")

    #time.sleep(1)

    #Except a title to contain substring
    WebDriverWait(driver, 10).until(EC.title_contains("SPORT BLAST - Hantle żeliwne, obciążenie, sztangi, gryfy"))

    #time.sleep(1)

    #Accept cookie policy
    confirm_button = driver.find_element(by = By.XPATH, value = "/html/body/div[6]/div[1]/div/div[1]/div[2]/button[2]").click()

    #time.sleep(1)
    

    driver.quit()