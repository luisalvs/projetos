import requests
from bs4 import BeautifulSoup

site = 'https://www.kabum.com.br/produto/229176'
headers = {
    "User-Agent": "Mozilla/5.0"
}

def enviar_telegram():
    token = '8316276492:AAE8FhmJ8HWMvTTd0MTNerRNgTcy92TslqE'
    chat_id = '2049824186'
    mensagem = f" O preço caiu para R$ {preco_desejado}! Veja: {site}"
    
    site_api = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {"chat_id": chat_id, "text": mensagem}
    requests.post(site_api, data=payload)

resposta = response = requests.get(site, headers=headers)
soup = BeautifulSoup(resposta.text, "lxml")

preco_element = soup.find("h4", class_="text-4xl text-secondary-500 font-bold transition-all duration-500")
preco = preco_element.text.strip().replace("R$", "").replace(".", "").replace(",", ".")

preco_float = float(preco)
print(f"Preço atual: R$ {preco}")

preco_desejado = 180.00

if preco_float <= preco_desejado:
    print("Preço abaixo do esperado! Enviar alerta!")
    enviar_telegram()
else:
    print('Preço ainda alto')
