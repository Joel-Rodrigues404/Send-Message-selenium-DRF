from selenium.webdriver.common.by import By
from rest_framework.views import APIView
from django.http import HttpResponse
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
            while (
                len(
                    navegador.find_elements(
                        By.XPATH,
                        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span',
                    )
                )
                < 1
            ):
                time.sleep(1)
            time.sleep(5)

            time.sleep(5)
            navegador.find_element(
                By.XPATH,
                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span',
            ).click()

            time.sleep(3)

            print("FIMM")

        return HttpResponse("deu bom")
