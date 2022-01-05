import time
import json
import os

from src.utils import *
from src.notify import send_message

import numpy as np
from PIL import Image
import nxbt


#nx = nxbt.Nxbt()
#controller_index = nx.create_controller(
#    nxbt.PRO_CONTROLLER,
#    reconnect_address=nx.get_switch_addresses())
#nx.wait_for_connection(controller_index)

# Activate controller and wait for Switch to recognize it
#nx.macro(controller_index, "B 0.1s\n 0.1s")
#nx.macro(controller_index, "B 0.1s\n 0.1s")
#nx.macro(controller_index, "B 0.1s\n 0.1s")

#press_button(nx, controller_index, "DPAD_RIGHT")
#press_button(nx, controller_index, "A")
#time.sleep(0.2)
#press_button(nx, controller_index, "DPAD_LEFT")
#press_button(nx, controller_index, "DPAD_RIGHT")

#time.sleep(10)
save_screenshot()
time.sleep(2)
save_screenshot()
time.sleep(2)
save_screenshot()
time.sleep(2)
save_screenshot()
save_screenshot()
save_screenshot()
save_screenshot()
save_screenshot()
save_screenshot()


hand_turtwig = np.array(Image.open("./check-imgs/hand-turtwig.png"))
hand_chimchar = np.array(Image.open("./check-imgs/hand-chimchar.png"))
hand_piplup = np.array(Image.open("./check-imgs/hand-piplup.png"))

TURTWIG = 0
CHIMCHAR = 1
PIPLUP = 2

pokemon = PIPLUP

mses = []
for i in range(50):
    img = get_image()
    height, width, _ = img.shape
    if pokemon == CHIMCHAR:
        xl = 0.46
        xr = 0.48
        yb = 0.5
        yt = 0.46
    elif pokemon == PIPLUP:
        xl = 0.65
        xr = 0.67
        yb = 0.35
        yt = 0.325
    else:
        xl = 0.325
        xr = 0.35
        yb = 0.35
        yt = 0.325
    img_area = relative_crop(img, xl, xr, yb, yt)

    if pokemon == CHIMCHAR:
        mses.append(mse(hand_chimchar, img_area))
    elif pokemon == PIPLUP:
        mses.append(mse(hand_piplup, img_area))
    else:
        mses.append(mse(hand_turtwig, img_area))

img_mse = np.min(mses)
print(f"Hand Select MSE: {img_mse}")

#img = get_image()
# Get the opponents health bar image region
#height, width, _ = img.shape
#xl = int(width * 0.90)
#xr = int(width * 0.96)
#yb = int(height * 0.12917)
#yt = int(height * 0.117)
#hp_bar = img[yt:yb, xl:xr, :]

# Get the mean of the hp bar
#red_mean = hp_bar[:,:,0:1].mean()
#green_mean = hp_bar[:,:,1:2].mean()
#blue_mean = hp_bar[:,:,2:3].mean()

#print(f'red_mean={red_mean} green_mean={green_mean} blue_mean={blue_mean}')

