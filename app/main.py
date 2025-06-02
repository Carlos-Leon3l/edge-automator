import os
from dotenv import load_dotenv, dotenv_values
from selenium import webdriver 
from selenium.webdriver.edge.options import Options
import selenium.webdriver.edge.service 
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
from faker import Faker
import random

def inicializa_automator(valor):

    faker = Faker()
    options = Options()
    load_dotenv()

    dotenv_values(".env")

    # O BASICO PARA APENAS A CONTA PRINCIPAL< TIRE PROFILE PARA DEFAULT
    
    options.add_argument("--user-data-dir=C:\\Users\\Carlos L\\AppData\\Local\\Microsoft\\Edge\\User Data")
    options.add_argument("--profile-directory=Default") 


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

    #print(driver.title)
    #print(driver.current_url)

    for repeat in range (0, valor):
        repeticao_de_busca_aleatoria()
        repeat = repeat + 1
        print(f"repetiu {repeat}")

    time.sleep(2)

    driver.quit()
    
if __name__ == "__main__":
    inicializa_automator()