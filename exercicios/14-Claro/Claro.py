# Necessário instalar: OpenCV e o Pillow - pip install opencv-python Pillow
import pyautogui  # Necessário instalar: pip install pyautogui
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

#Código antigo para mostrar a localização da imagem
#onde_clicar = None
#clicar_no_x = None
navegador = int(tk.simpledialog.askstring("Para Firefox digite 1, para Chrome digite 2", "Selecione o navegador:"))

def tem_x_imagem(img):

    while True:

        try:
            #Código antigo para mostrar a localização da imagem            
            #clicar_no_x = pyautogui.locateOnScreen(img, confidence=0.8)
            #print(f"Found at: {clicar_no_x}")
            
            if pyautogui.locateOnScreen(img, confidence=0.9):
                print(f"Imagem '{img}' encontrada!")
                pyautogui.sleep(4)
                pyautogui.click(1333,107)
                break
        except:
            pyautogui.click(556, 268)
            pyautogui.sleep(10)
    pyautogui.sleep(1)
    
def wait_for_image(img):

    while True:

        try:
            #Código antigo para mostrar a localização da imagem            
            #onde_clicar = pyautogui.locateOnScreen(img, confidence=0.8)
            #print(f"Found at: {onde_clicar}")
            
            if pyautogui.locateOnScreen(img, confidence=0.9):
                print(f"Imagem '{img}' encontrada!")
                break
        except:
            print(
                f"Erro ao procurar a imagem '{img}'. Verifique o caminho e tente novamente.")
            pyautogui.sleep(3)
    pyautogui.sleep(1)


pyautogui.sleep(1)
pyautogui.hotkey('win', 'r')
pyautogui.sleep(1)  # Espera 1 segundo

if navegador == 1:
    pyautogui.typewrite('firefox')
elif navegador == 2:
    pyautogui.typewrite('chrome')
    
pyautogui.press('enter')
""" pyautogui.sleep(3)  # Espera 1 segundo
pyautogui.hotkey('ctrl', '4')
# Substitua 'resgatar.png' pela imagem que representa o a página abert
pyautogui.hotkey('alt', 'tab')  # Alterna para a janela do navegador
wait_for_image('claro.png')
pyautogui.sleep(2)  # Espera 1 segundo
wait_for_image('pontuar.png')
pyautogui.sleep(5)
pyautogui.click(852,672)
pyautogui.sleep(5)  # Espera 1 segundo
pyautogui.click(556, 268)  # Clica na posição específica
pyautogui.sleep(3)  # Espera 1 segundo
tem_x_imagem('x.png')
tem_x_imagem('x.png')
tem_x_imagem('x.png')
tem_x_imagem('x.png')
tem_x_imagem('x.png')
 """
# Código antigo para mostrar a localização do mouse
#x, y = pyautogui.position()
#print("x = "+str(x)+" y = "+str(y))



