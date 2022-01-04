import time
import json
import os

from src.utils import *
from src.notify import send_message

import numpy as np
from PIL import Image
import nxbt


nx = nxbt.Nxbt()
controller_index = nx.create_controller(
    nxbt.PRO_CONTROLLER,
    reconnect_address=nx.get_switch_addresses())
nx.wait_for_connection(controller_index)

# Activate controller and wait for Switch to recognize it
nx.macro(controller_index, "B 0.1s\n 0.1s")
nx.macro(controller_index, "B 0.1s\n 0.1s")
nx.macro(controller_index, "B 0.1s\n 0.1s")

#press_button(nx, controller_index, "DPAD_RIGHT")
press_button(nx, controller_index, "A")
#time.sleep(2)
#press_button(nx, controller_index, "DPAD_LEFT")

#time.sleep(10)
img = get_image()
img = get_image()
img = get_image()
img = get_image()
img = get_image()
img = get_image()
img = get_image()
img = get_image()
img = get_image()
img = get_image()
