import os
from dotenv import load_dotenv
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from faker import Faker
import random

def inicializa_automator(valor):
    faker = Faker()
    options = webdriver.EdgeOptions()
    load_dotenv(override=True)  

    USER_DATA_DIR = os.getenv("COUNT_MICROSOFT")
    PROFILE_DIR = os.getenv("USER_PROFILE")

    print("User Data:", USER_DATA_DIR)
    print("Profile Dir:", PROFILE_DIR)

    options = webdriver.EdgeOptions()
    options.add_argument(f"--user-data-dir={USER_DATA_DIR}")
    options.add_argument(f"--profile-directory={PROFILE_DIR}")
    # Inicia o WebDriver
    driver = webdriver.Edge(options=options)

    Faker.seed(random.randint(1,99))  
    palavras = faker.words(nb=100)
    print(palavras)
    def pega_palavra(palavras:list): 
        return palavras.pop(0)

    def repeticao_de_busca_aleatoria():
        
        driver.switch_to.new_window('tab')
        
        time.sleep(2)

        driver.get('https://www.bing.com/?scope=web&cc=BR&FORM=ANNTH1&pc=U531')
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/form/div[1]/div/textarea").click()
        
        time.sleep(3)
        
        lista_palavras = pega_palavra(palavras)
        for palavra in lista_palavras:
            driver.find_element(By.XPATH,'//*[@id="sb_form_q"]').send_keys(palavra)
            time.sleep(0.3)
            
        print(f"passou no for a palavras {lista_palavras}")

        time.sleep(3)

        driver.find_element(By.XPATH,'//*[@id="search_icon"]').click()
        
        time.sleep(3)

    for repeat in range (0, valor):
        repeticao_de_busca_aleatoria()
        repeat = repeat + 1
        print(f"repetiu {repeat}")

    time.sleep(2)

    driver.quit()
    
if __name__ == "__main__":
    inicializa_automator()