import pyautogui as pag 
import random
import time
import sys

try:
   while True:
        x = random.randint(600,700) #coordenada x
        y = random.randint(200,600) #coordenada y
        pag.moveTo(x,y,0.5)
        time.sleep(2)
except KeyboardInterrupt:
    sys.exit('fechando') #Pressione ctrl + c