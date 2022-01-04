from src.utils import *
import os

import nxbt

# Initialize an emulated controller and connect
# to an available Switch.
nx = nxbt.Nxbt()
controller_index = nx.create_controller(
    nxbt.PRO_CONTROLLER,
    reconnect_address=nx.get_switch_addresses())
nx.wait_for_connection(controller_index)

# Activate controller and wait for Switch to recognize it
nx.macro(controller_index, "B 0.1s\n 0.1s")
nx.macro(controller_index, "B 0.1s\n 0.1s")
nx.macro(controller_index, "B 0.1s\n 0.1s")

press_button(nx, controller_index, "HOME")
time.sleep(2)
press_button(nx, controller_index, "X")
time.sleep(2)
press_button(nx, controller_index, "A")
