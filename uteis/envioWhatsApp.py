from uteis.mySelenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

url = "https://web.whatsapp.com/"

navegador = webdriver.Firefox()
navegador.get(url)

while len(navegador,find_elements('id', 'side')) < 1:
    time.sleep(1)

for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}" 
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('path da mensagem do whatsapp').send_keys(Keys.ENTER) 
    time.sleep(10)   