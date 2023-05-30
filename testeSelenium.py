from selenium import webdriver
from time import sleep

driver = webdriver.Edge(
    r'C:\Users\USUÁRIO\Desktop\python3_basico_avancado3\aula193\drivers\msedgedriver.exe'
)

driver.get('https://www.google.com.br/')
sleep(10)