import pyautogui
import time

pyautogui.alert("O código está rodando. Não use o computador durante a execução do programa.")
pyautogui.PAUSE = 0.5

# abre o google drive
pyautogui.click(x=34,y=63)
time.sleep(1)
pyautogui.hotkey("ctrlleft", "t")
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/u/0/my-drive")
pyautogui.press("enter")

# abre o explorador de arquivos
pyautogui.click(x=34,y=131)
time.sleep(1)

# mostra o conteudo da area de trabalho
pyautogui.click(x=246,y=245)


# clica no arquivo que quero fazer o upload
pyautogui.click(x=495,y=136)


# arrasta o arquivo para o google drive
pyautogui.dragTo(1067, 730, 1, button='left')
pyautogui.mouseUp()

# esperar 5 segundos para fazer o upload do arquivo
time.sleep(5)

pyautogui.alert("O programa já finalizou! Computador liberado para uso.")
