import os
import pyautogui as pa
import time
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

load_dotenv()
#Senha x=387, y=445

#A partir dos -- são especificacoes para abrir exatamente o que precisa, no caso o jogo correto e o patch atual ao inves do PBE
lol = r'"C:\Riot Games\Riot Client\RiotClientServices.exe" --launch-product=league_of_legends --launch-patchline=live'
os.system(lol)

time.sleep(8)

bt_login = pa.click (x=395, y=380, button='left', clicks=1)

Campo_Login = os.getenv('login')
if Campo_Login:
    pa.write(Campo_Login)
else:
    print("Erro no login!.")

senha = pa.click (x=387, y=445, button='left', clicks=1)

Campo_Login = os.getenv('senha')
if Campo_Login:
    pa.write(Campo_Login)
else:
    print("Erro na senha.")

botao_entrar = pa.click(x=389, y=767, clicks=1, button='left')

time.sleep(5)
botao_jogar = pa.click(x=408, y=404, clicks=1, button='left')
print('Deu certo!')