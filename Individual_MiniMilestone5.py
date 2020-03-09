# Owen Johnstone November 5, 2019

import math
def objective1(FL, SL):
    fl_input = FL[0]
    fl_output = FL[-1]
    sl_input = SL[0]
    sl_output = SL[-1]
    fl_gear_ratio = fl_output / fl_input
    sl_gear_ratio = sl_output / sl_input
    gear_ratio = fl_gear_ratio * sl_gear_ratio
    return gear_ratio

def objective4():
    length = 36
    positions = []
    for angle in range(0, 100, 10):
        point = [-length * math.cos(math.radians(angle)), 36 - (length * math.sin(math.radians(angle)))]
        positions.append(point)
    return positions
