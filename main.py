import os
from dotenv import load_dotenv, dotenv_values
from selenium import webdriver 
from selenium.webdriver.edge.options import Options
import selenium.webdriver.edge.service 
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

load_dotenv()

config = dotenv_values(".env")

lista_palavras = ["sujeira", "almoço", "abacaxi", "janela", "carro bmw", "ortopedista", "paralelepipedo", "carruagem", "chapolin", "jogo do betis hoje"]

options = Options()

options.add_argument(os.getenv("COUNT_MICROSOFT"))
options.add_argument('profile-directory=Default')

driver = webdriver.Edge(options=options)

def pega_palavra(lista_palavras: list):
    return lista_palavras.pop(0)

def repeticao_de_busca_aleatoria():
    
    driver.switch_to.new_window('tab')
    
    time.sleep(2)

    driver.get('https://www.bing.com/?scope=web&cc=BR&FORM=ANNTH1&pc=U531')
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/form/div[1]/div/textarea").click()
    
    print("passou aqui 1")
    
    time.sleep(3)
    
    palavra = pega_palavra(lista_palavras)
    for letras in palavra:
        driver.find_element(By.XPATH,'//*[@id="sb_form_q"]').send_keys(letras)
        time.sleep(0.3)
        
    print("passou aqui 2")

    time.sleep(3)

    driver.find_element(By.XPATH,'//*[@id="search_icon"]').click()
    print("passou aqui 3")
    
    time.sleep(3)

#print(driver.title)
#print(driver.current_url)

for repeat in range (0, 10):
    repeticao_de_busca_aleatoria()
    repeat = repeat + 1
    print(f"repetiu {repeat}")

time.sleep(5)

driver.quit()