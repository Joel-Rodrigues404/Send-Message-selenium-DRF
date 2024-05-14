import time
from selenium.webdriver.common.by import By
# import pandas as pd
from selenium import webdriver
import urllib
# import os

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com")

# esperar a tela do whatsapp carregar
while len(navegador.find_elements(By.ID, 'side')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
    print('--=-=-=-AQUI0-=-=-=-=-==')
    time.sleep(1)
time.sleep(2)  # só uma garantia

# o whatsapp já carregou

for _ in range(2):
    time.sleep(3)
    # enviar uma mensagem para a pessoa
    nome = 'joel'
    mensagem = 'olá'
    arquivo = ''
    telefone = '5588996249647'

    texto = mensagem.replace("fulano", nome)
    texto = urllib.parse.quote(texto)

    # enviar a mensagem
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
    # link = " https://web.whatsapp.com/send?phone=5588996249647&text=texto"

    navegador.get(link)
    # esperar a tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
    while len(navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
        # while len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/div[2]/header/div')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
        print('--=-=-=-AQUI-=-=-=-=-==')
        time.sleep(1)
    time.sleep(5)  # só uma garantia
    print('--=-=-=-AQUI2-=-=-=-=-==')
    
    time.sleep(5)
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()
    print('--=-=-=-AQUI3-=-=-=-=-==')

    time.sleep(3)

    print('FIMM')
