import requests
from bs4 import BeautifulSoup

def rastrear_preco(url, preco_alvo):
    cabecalhos = {"User-Agent": "Mozilla/5.0"}
    resposta = requests.get(url, headers=cabecalhos)
    sopa = BeautifulSoup(resposta.content, 'html.parser')
    preco = float(sopa.find("span", {"class": "preco"}).text.replace('R$', '').replace(',', '').replace('.', ''))
    if preco <= preco_alvo:
        print("Preço abaixo do alvo:", preco)
    else:
        print("Preço atual:", preco)

rastrear_preco('URL_DO_PRODUTO', 100.00)
