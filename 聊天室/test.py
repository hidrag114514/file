import win32gui
import time
from pynput.mouse import Listener
def on_click(x,y,button,pressed):
    if pressed:
        print(button)
with Listener(on_click=on_click) as listener:
    listener.join()

