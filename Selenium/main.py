from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup # transforma em um objeto python para manipulação
import time


browser = webdriver.Firefox()
browser.get('https://efisco.sefaz.pe.gov.br/sfi_trb_gpf/PRConsultarDevedoresInscritosEmDividaAtiva')

select_element = browser.find_element('id', 'primeiro_campo')
select = Select(select_element)

select.select_by_visible_text("CPF")
browser.find_element('id', 'NuDocumentoIdentificacao').send_keys('054.024.674-39')
browser.find_element('id', 'btt_localizar').click()

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
dados = soup.find_all('div', class_='tabeladados')

for dado in dados:
    print(dado.text)
    
browser.quit()