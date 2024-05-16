from selenium.webdriver.common.by import By
from rest_framework.views import APIView
from django.http import HttpResponse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import urllib
import time
import os

NUM = str(os.getenv("NUM"))


class SendMessage(APIView):

    def get(self, request, *args, **kwargs):
        navegador = webdriver.Chrome()
        navegador.get("https://web.whatsapp.com")

        while len(navegador.find_elements(By.ID, "side")) < 1:
            time.sleep(1)
        time.sleep(2)

        for _ in range(2):
            time.sleep(3)
            nome = "joel"
            mensagem = "olá"
            telefone = NUM

            texto = mensagem.replace("fulano", nome)
            texto = urllib.parse.quote(texto)

            link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"

            navegador.get(link)
            while (len(navegador.find_elements(
                    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span',)) < 1):
                time.sleep(1)
            time.sleep(5)

            navegador.find_element(
                By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span',).click()

            time.sleep(3)

        return HttpResponse("deu bom")


class SendChannel(APIView):

    def get(self, request, *args, **kwargs):
        # Abri navegador
        navegador = webdriver.Chrome()
        navegador.get("https://web.whatsapp.com")

        while len(navegador.find_elements(By.ID, "side")) < 1:
            time.sleep(1)
        time.sleep(2)

        # Clicar no icone de canais
        navegador.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/header/div/div/div/div/span/div/div[1]/div[4]/div/span').click()
        time.sleep(2)
        # Clicar no canal

        # Localizar o canal pelo texto e clicar
        texto_do_canal = "SysEleições"  # Substitua pelo texto do canal específico

        # Localizar o canal pelo texto e clicar usando CSS Selector
        canal_css = f'span[title="{texto_do_canal}"]'
        elemento_canal = WebDriverWait(navegador, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, canal_css)))
        elemento_canal.click()
        time.sleep(2)
        
        # confirma canal
        navegador.find_element(By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div/button[2]/div/div').click()
        time.sleep(4)
        # capturar mensagem do usuario da pra fazer por url
        caixa_texto = navegador.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
        )
        mensagem = 'Mensagem'
        caixa_texto.send_keys(mensagem)
        caixa_texto.send_keys(Keys.ENTER)
        time.sleep(5)
        # Enviar

        return HttpResponse("deu bom")
