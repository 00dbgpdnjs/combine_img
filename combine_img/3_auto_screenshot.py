# Compare with 6_advanced_screenshot.py
# Start this program -> pause 5s to set up[open window to capture] -> Capture the screen and save as a file in same dir  every 2s total 10 times

import time
from PIL import ImageGrab  # PIL : Python Image Library / $ pip install pillow

time.sleep(5)

for i in range(1, 11):  # To save 10 imgs
    img = ImageGrab.grab()  # Save screenshot in "img"
    # Save as a file / the arg : file name : image1.png ~ image10.png
    img.save("image{}.png".format(i))
    time.sleep(2)
