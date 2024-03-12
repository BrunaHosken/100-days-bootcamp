# Automate some aspect of your life using Python.

import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def perform_random_google_search():
    search_terms = ["pizza", "sushi", "burger", "pasta", "ice cream", "chocolate", "salad"]

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")


    driver = webdriver.Chrome(options=chrome_options)

    try:
        for _ in range(5):
            search_term = random.choice(search_terms)
            search_url = f"https://www.google.com/search?q={search_term}"

            driver.get(search_url)
            
            # Adicione uma espera explícita para garantir que o campo de pesquisa esteja presente
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
            
            # Introduza atrasos aleatórios para simular o comportamento humano
            time.sleep(random.uniform(3, 6))

            first_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.r a'))
            )
            first_link.click()

            # Aguarde 10 segundos após clicar no link
            time.sleep(10)

            driver.back()

            # Aguarde alguns segundos antes de realizar a próxima pesquisa
            time.sleep(random.uniform(3, 6))

    finally:
        driver.quit()

if __name__ == "__main__":
    perform_random_google_search()
