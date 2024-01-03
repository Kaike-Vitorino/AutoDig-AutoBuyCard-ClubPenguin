# Definir area da mineracao - 749,640 - 1143,854
# Clicar em algum lugar da area a cada 36 segundos
# Clicar no botao de perfil proprio
# Clicar no botao de dancas
# Clicar no botao da danca de cima para minerar
# Clicar no botao do puffle
# Clicar no botao de tesouro do puffle
# Esperar 25 segundos para trocar de lugar

import pyautogui
import random
import time
import keyboard

# Definindo a area
x1, y1 = 749, 640
x2, y2 = 1143, 854

while True:

    # Se clicar no F1, o negocio para
    if keyboard.is_pressed('F1'):  # se a tecla F1 for pressionada, o programa será interrompido
        break

    # Escolhendo o proximo local de clique aleatorio
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)

    # Movendo o mouse para a coordenada gerada e realizando o clique
    pyautogui.moveTo(x, y)
    pyautogui.click(duration=1)

    # Clicar no botao de perfil proprio
    pyautogui.click(1223,931,duration=1)

    # Clicar no botao de dancas e em seguida na danca
    pyautogui.click(629,933, duration=1)
    pyautogui.click(619,636, duration=1)

    # Clicar no botao do puffy e em seguida no presente dele
    pyautogui.click(527,931, duration=1)
    pyautogui.click(540,830, duration=1)

    # Esperar alguns segundo para que seja trocado de local
    time.sleep(15)  # você pode ajustar o intervalo de tempo aqui


