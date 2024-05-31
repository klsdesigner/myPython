# %%
# Importar as bibliotecas 
# clicar no botão "Bater ponto"
# depois clicar no outro botão tmb "Bater ponto"
# depois do ponto registrado enviar uma mensagem para o whatsapp
# clicar em "Meu ponto"

# ========================================================================
# ================== PASSO PARA AUTOMATIZAR O PONTO MAIS =================
# ========================================================================

import pyautogui as pg
from datetime import datetime, timedelta
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# entrar no site ponto mais url: 'https://app2.pontomais.com.br/meu-ponto'
url = "https://app2.pontomais.com.br/meu-ponto"

browser.maximize_window()
browser.get(url)

# fazer login no ponto mais
login_email = "kleber.souza@klios.com.br"
senha = "Kleber@2023"

time.sleep(0.7)  
browser.find_element('xpath', '/html/body/app-root/dx-drawer/div/div[2]/div[2]/div/login/div/div[1]/div/div[4]/div[1]/login-form/pm-form/form/div/div/div[1]/pm-input/div/div/pm-text/div/input').send_keys(login_email)
time.sleep(0.7) 
browser.find_element('xpath', '/html/body/app-root/dx-drawer/div/div[2]/div[2]/div/login/div/div[1]/div/div[4]/div[1]/login-form/pm-form/form/div/div/div[2]/pm-input/div/div/pm-password/div/input').send_keys(senha) 
time.sleep(0.7)
browser.find_element('xpath', '/html/body/app-root/dx-drawer/div/div[2]/div[2]/div/login/div/div[1]/div/div[4]/div[1]/login-form/pm-button[1]/button').click() 


# %%
time.sleep(3)

# checar horas atual com a lista de horarios
hoje = datetime.now()

baterPonto1 = '/html/body/app-root/app-side-nav-outer-toolbar/app-header/header/dx-toolbar/div/div[3]/div[2]/dxi-item/pm-button/button'
baterPonto2 = '/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/app-container/time-card-register/div/div[2]/div[2]/pm-time-card-register/pm-card/div/div[2]/div[1]/div[2]/div/pm-button/button'
pausa1 = '/html/body/app-root/app-side-nav-outer-toolbar/app-header/header/dx-toolbar/div/div[3]/div[1]/dxi-item/pm-button'
pausa2 = '/html/body/app-root/app-side-nav-outer-toolbar/dx-drawer/div/div[2]/dx-scroll-view/div[1]/div/div[1]/div[2]/div[1]/app-container/pm-nr17/div/div[2]/div[2]/pm-card/div/div[2]/div/div[3]/pm-button/button'

## Entrada ===========================================
## ===================================================
if hoje.strftime("%H:%M") == "17:07":
    # Bater ponto 1
    browser.find_element('xpath', baterPonto1).click()
    time.sleep(1)
    # Bater ponto 2
    browser.find_element('xpath', baterPonto2).click()    

## saida para almoço =================================
## ===================================================
if hoje.strftime("%H:%M") == "12:30":
    # Bater ponto 1
    browser.find_element('xpath', baterPonto1).click()
    time.sleep(1)
    # Bater ponto 2
    browser.find_element('xpath', baterPonto2).click()

## retorno do almoço ==================================
## ====================================================
if hoje.strftime("%H:%M") == "13:30":
    # Bater ponto 1
    browser.find_element('xpath', baterPonto1).click()
    time.sleep(1)
    # Bater ponto 2
    browser.find_element('xpath', baterPonto2).click()

## saida para lanche =================================
## ===================================================
if hoje.strftime("%H:%M") == "16:00":
    browser.find_element('xpath', pausa1)
    time.sleep(1)
    browser.find_element('xpath', pausa2)

## retorno do lanche =================================
## ===================================================
if hoje.strftime("%H:%M") == "16:15":     
    browser.find_element('xpath', pausa1).click()
    time.sleep(1)
    browser.find_element('xpath', pausa2).click()
    

## Saida =============================================
## ===================================================
if hoje.strftime("%H:%M") == "17:45":     
    browser.find_element('xpath', baterPonto1).click()
    time.sleep(1)
    browser.find_element('xpath', baterPonto2).click()


# %%
## Conferência fianl =================================
## ===================================================
time.sleep(10)
meuPonto = '//*[@id="dx-c9d27185-58c4-9dd1-39c3-06bd5ddce436"]/div/div/a'
acaoSeta = '//*[@id="gridContainer"]/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[10]/div/div/a/pm-drop-down/a/div/pm-button/button'
acaoHistorico = '//*[@id="gridContainer"]/div/div[6]/div/div/div[1]/div/table/tbody/tr[1]/td[10]/div/div/a/pm-drop-down/a/div/div/a[2]'


browser.find_element('xpath', meuPonto).click()
time.sleep(2)
browser.find_element('xpath', acaoSeta).click()
time.sleep(2)
browser.find_element('xpath', acaoHistorico).click()
#browser.quit()


