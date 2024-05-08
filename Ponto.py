# Aqui importamos o conteúdo usado para o batedor de pontos
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time
import random


# Aqui montamos a função que irá automatizar a batida do ponto
def batedor_de_ponto():
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument("start-maximized")
    chromeoptions.add_argument("--use-fake-ui-for-media-stream")
    driver = webdriver.Chrome(options=chromeoptions)
    url = 'https://app.tangerino.com.br/Tangerino/pages/baterPonto/'
    driver.get(url)
    time.sleep(5)
    driver.find_element(By.ID, 'codigoEmpregador').send_keys('FZB31')
    #driver.find_element(By.ID, 'codigoPin').send_keys('8621', Keys.ENTER)
    time.sleep(3)


# Aqui temos os parametros de randomização do minuto e segundo
minute = 20, 21, 22, 23, 24, 25, 26, 27, 28, 29
sec = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59
minute_almoco = 0, 1, 2, 3, 4, 5
minute_volta = 25, 26, 27, 28, 29, 30
minute_fim = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# Aqui de fato estamos randomizando após o cadastro das bibliotecas
rand_min = random.choice(minute)
rand_sec = random.choice(sec)
rand_min_almoco = random.choice(minute_almoco)
rand_min_volta = random.choice(minute_volta)
rand_min_fim = random.choice(minute_fim)

# Aqui temos os batedores conforme a aleatoriedade
batedor_manha = datetime.time(8, rand_min, rand_sec)
batedor_almoco = datetime.time(12, rand_min_almoco, rand_sec)
batedor_volta_almoco = datetime.time(13, rand_min_volta, rand_sec)
batedor_final_dia = datetime.time(18, rand_min_fim, rand_sec)
# Aqui estamos transformando cada batedor em string para podermos trabalhar com operadores (>, <, ==, !=, etc)
a = batedor_manha.strftime("%X")
b = batedor_almoco.strftime("%X")
c = batedor_volta_almoco.strftime("%X")
d = batedor_final_dia.strftime("%X")
# Linhas para fins de teste
batedor_teste = datetime.time(21, 44, 30)
batedor_teste1 = datetime.time(21, 45, 2)
# Aqui transformamos o batedor_teste em string para poder fazer operações logicas (+, -, /, *, ==, !=, etc)
x = batedor_teste.strftime("%X")
y = batedor_teste1.strftime("%X")

while True:
    dataehora = datetime.datetime.now()
    hora = dataehora.strftime("%X")
    if hora == a:
        batedor_de_ponto()
    if hora == b:
        batedor_de_ponto()
    if hora == c:
        batedor_de_ponto()
    if hora == d:
        batedor_de_ponto()
    if hora == x:
        batedor_de_ponto()
    if hora == y:
        batedor_de_ponto()
