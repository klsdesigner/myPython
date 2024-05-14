# ========================================================================
# ================== PASSO PARA AUTOMATIZAR O PONTO MAIS =================
# ========================================================================

# Importar as bibliotecas 
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

# checar horas atual com a lista de horarios
horarios = ['08:00','12:30','13:30','16:00','16:15','17:45',]

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

# time.sleep(2)

# browser.find_element('xpath', '/html/body/app-root/app-side-nav-outer-toolbar/app-header/header/dx-toolbar/div/div[3]/div[2]/dxi-item/pm-button/button').click() 


# time.sleep(3)
# print(browser.get())






# browser.find_element('xpath', '/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[4]/a/div/img').click() 

# browser.find_element('xpath', '/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[4]/a/div/img').click() 


# clicar no botão "Bater ponto"
# depois clicar no outro botão tmb "Bater ponto"
# depois do ponto registrado enviar uma mensagem para o whatsapp
# clicar em "Meu ponto"

#browser.quit()
