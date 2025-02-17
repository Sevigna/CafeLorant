import pyautogui
import time
import pystray
from Variable import *

#################################### Fonctions ####################################
def Astra():
    i = 0
    while True:
        if pyautogui.locateOnScreen(AstraImg, grayscale=False, confidence=0.7):
            AstraLocation = pyautogui.locateCenterOnScreen('Assets/astra.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(AstraLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Breach():
    i = 0
    while True:
        if pyautogui.locateOnScreen(BreachImg, grayscale=False, confidence=0.7):
            BreachLocation = pyautogui.locateCenterOnScreen('Assets/breach.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(BreachLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Brimstone():
    i = 0
    while True:
        if pyautogui.locateOnScreen(BrimstoneImg, grayscale=False, confidence=0.7):
            BrimstoneLocation = pyautogui.locateCenterOnScreen('Assets/brimstone.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(BrimstoneLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Chamber():
    i = 0
    while True:
        if pyautogui.locateOnScreen(ChamberImg, grayscale=False, confidence=0.7):
            ChamberLocation = pyautogui.locateCenterOnScreen('Assets/chamber.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(ChamberLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Cypher():
    i = 0
    while True:
        if pyautogui.locateOnScreen(CypherImg, grayscale=False, confidence=0.7):
            CypherLocation = pyautogui.locateCenterOnScreen('Assets/cypher.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(CypherLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Fade():
    i = 0
    while True:
        if pyautogui.locateOnScreen(FadeImg, grayscale=False, confidence=0.7):
            FadeLocation = pyautogui.locateCenterOnScreen('Assets/fade.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(FadeLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Harbor():
    i = 0
    while True:
        if pyautogui.locateOnScreen(HarborImg, grayscale=False, confidence=0.7):
            HarborLocation = pyautogui.locateCenterOnScreen('Assets/harbor.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(HarborLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Jett():
    i = 0
    while True:
        if pyautogui.locateOnScreen(JettImg, grayscale=False, confidence=0.7):
            JettLocation = pyautogui.locateCenterOnScreen('Assets/jett.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(JettLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Kayo():
    i = 0
    while True:
        if pyautogui.locateOnScreen(KayoImg, grayscale=False, confidence=0.7):
            KayoLocation = pyautogui.locateCenterOnScreen('Assets/kayo.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(KayoLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Killjoy():
    i = 0
    while True:
        if pyautogui.locateOnScreen(KilljoyImg, grayscale=False, confidence=0.7):
            KilljoyLocation = pyautogui.locateCenterOnScreen('Assets/killjoy.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(KilljoyLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Neon():
    i = 0
    while True:
        if pyautogui.locateOnScreen(NeonImg, grayscale=False, confidence=0.7):
            NeonLocation = pyautogui.locateCenterOnScreen('Assets/neon.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(NeonLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Omen():
    i = 0
    while True:
        if pyautogui.locateOnScreen(OmenImg, grayscale=False, confidence=0.7):
            OmenLocation = pyautogui.locateCenterOnScreen('Assets/omen.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(OmenLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Phoenix():
    i = 0
    while True:
        if pyautogui.locateOnScreen(PhoenixImg, grayscale=False, confidence=0.7):
            PhoenixLocation = pyautogui.locateCenterOnScreen('Assets/phoenix.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(PhoenixLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Raze():
    i = 0
    while True:
        if pyautogui.locateOnScreen(RazeImg, grayscale=False, confidence=0.7):
            RazeLocation = pyautogui.locateCenterOnScreen('Assets/raze.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(RazeLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Reyna():
    i = 0
    while True:
        if pyautogui.locateOnScreen(ReynaImg, grayscale=False, confidence=0.7):
            ReynaLocation = pyautogui.locateCenterOnScreen('Assets/reyna.png', grayscale=False, confidence = 0.7)
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(ReynaLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur Reyna')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Sage():
    i = 0
    while True:
        if pyautogui.locateOnScreen(SageImg, grayscale=False, confidence=0.7):
            SageLocation = pyautogui.locateCenterOnScreen('Assets/sage.png', grayscale=False, confidence = 0.7)
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(SageLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Skye():
    i = 0
    while True:
        if pyautogui.locateOnScreen(SkyeImg, grayscale=False, confidence=0.7):
            SkyeLocation = pyautogui.locateCenterOnScreen('Assets/skye.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(SkyeLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Sova():
    i = 0
    while True:
        if pyautogui.locateOnScreen(SovaImg, grayscale=False, confidence=0.7):
            SovaLocation = pyautogui.locateCenterOnScreen('Assets/sova.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(SovaLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0


def Viper():
    i = 0
    while True:
        if pyautogui.locateOnScreen(ViperImg, grayscale=False, confidence=0.7):
            ViperLocation = pyautogui.locateCenterOnScreen('Assets/viper.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(ViperLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0

def Yoru():
    i = 0
    while True:
        if pyautogui.locateOnScreen(YoruImg, grayscale=False, confidence=0.7):
            YoruLocation = pyautogui.locateCenterOnScreen('Assets/yoru.png', grayscale=False, confidence = 0.7)
            pyautogui.moveTo(YoruLocation)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            pyautogui.moveTo(LockPos)
            pyautogui.PAUSE = 0.1
            pyautogui.leftClick()
            pyautogui.PAUSE = 0.1
            break
        else:
            if i != 5000:
                print('erreur')
                time.sleep(0.1)
                i+=1
            else:
                break
    print('Délai terminé, vous pouvez rechoisir un agent.')
    i = 0
###################################################################################