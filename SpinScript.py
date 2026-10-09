import time
import threading
from pynput.keyboard import Key, Controller
import random

inTheMiddleOfSpinning = False
spin = True
waitTimeMin: float = 0.03500
waitTimeMax: float = 0.05000

keyboard = Controller()



def Spin():
    global spin
    global inTheMiddleOfSpinning
    inTheMiddleOfSpinning = True
    while spin:
        keyboard.press("w")
        time.sleep(random.uniform(waitTimeMin, waitTimeMax))
        keyboard.release("a")
        time.sleep(random.uniform(waitTimeMin, waitTimeMax))
        keyboard.press("d")
        time.sleep(random.uniform(waitTimeMin, waitTimeMax))
        keyboard.release("w")
        time.sleep(random.uniform(waitTimeMin, waitTimeMax))
        keyboard.press("s")
        time.sleep(random.uniform(waitTimeMin, waitTimeMax))
        keyboard.release("d")
        time.sleep(random.uniform(waitTimeMin, waitTimeMax))
        keyboard.press("a")
        time.sleep(random.uniform(waitTimeMin, waitTimeMax))
        keyboard.release("s")
        time.sleep(random.uniform(waitTimeMin, waitTimeMax))
    else:
        inTheMiddleOfSpinning = False
        print("Stopped Spinning")

def stopSpin():
    global spin
    global inTheMiddleOfSpinning
    spin = False
    while inTheMiddleOfSpinning:
        time.sleep(0.02)
        keyboard.release("a")
        keyboard.release("w")
        keyboard.release("d")
        keyboard.release("s")
    else:
        print("Stopping Inputs")
        keyboard.release("a")
        keyboard.release("w")
        keyboard.release("d")
        keyboard.release("s")




def startSpin():
    global spin
    spin = True
    spinThread = threading.Thread(target=Spin)
    spinThread.start()



