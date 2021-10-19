# 3_auto_screenshot.py is operated according to time
# Otherwise this file is operated according to hotkey i.e when I want

import time
import keyboard  # keyboard module : Process based on keyboard # $ pip install keyboard
from PIL import ImageGrab


def screenshot():
    # 2021년 10월 17일 4시 47분 30초 -> _20211017_164730
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))  # ex) image_20211017_164730.png


# hotkey = keyboard shortcut / 1st arg : a or ctrl+shift+s etc
keyboard.add_hotkey("F9", screenshot)

keyboard.wait("esc")  # Run this program until pressing the key, esc
