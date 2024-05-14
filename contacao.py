import requests
from datetime import datetime, time
import pyautogui
import time

hoje = datetime.now()
horasExec = ["10:20", "10:30", "10:40", "16:50"]

if hoje.strftime("%H:%M") in horasExec:

    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    # print(f"Cotação Atualizada. {datetime.now()}\nDolar: R${cotacao_dolar}\nEuro: R${cotacao_euro}\nBTC: R${cotacao_btc}")

    # Para rodar sem parar pode-se usar: google cloud, aws, azure, heroku (100% gratis)
    time.sleep(1)
    # print(pyautogui.position())
    pyautogui.press('win')
    pyautogui.write("bloco de Notas")    
    pyautogui.press("enter")

    time.sleep(0.6)
    pyautogui.write(f"Cotação Atualizada.\n\nData: {hoje.strftime("%d/%m/%Y %H:%M:%S")}\n\nDolar: R$ {cotacao_dolar}\nEuro: R$ {cotacao_euro}\nBTC: R$ {cotacao_btc}")

else:
    print(f"Ainda não esta no horario, são: {hoje.strftime("%H:%M")}")    

time.sleep(2)
print(f"Fim script as: {hoje.strftime("%H:%M")}")