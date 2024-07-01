import threading
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode, Listener

TOGGLE_KEY = KeyCode(char="q")

clicking = False
mouse = Controller()


def clicker():
    while True:
        if clicking:
            mouse.click(Button.left)
        time.sleep(0.005)


def toggle_clicking(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


thread = threading.Thread(target=clicker)
thread.start()

with Listener(on_press=toggle_clicking) as listener:
    listener.join()