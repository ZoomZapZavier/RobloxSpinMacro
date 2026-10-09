from pynput import keyboard
import SpinScript
import time
spin = False

def toggleSpin():
    global spin
    if spin == True:
        spin = False
    else:
        spin = True

def on_press(key):
    try:

        if key.char == "c":
            toggleSpin()
            if spin:
                SpinScript.startSpin()
                print("Sending Command to stop")
            else:
                SpinScript.stopSpin()
                print("Sending Command to start")
            time.sleep(0.5)

    except AttributeError:
        ...

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

