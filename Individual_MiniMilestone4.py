# Name: Owen Johnstone
# Student Number: 
# Date: October 29, 2019

import math

def objective2(gear_ratio):
    finger_rev = 90 / 360
    input_rotations = finger_rev * gear_ratio
    return input_rotations

def objective4(inp_speed, gear_ratio):
    distance_rotated = 90 *  math.pi / 180
    output_speed_rpm = inp_speed / gear_ratio
    output_speed_rad = output_speed_rpm * 2 * math.pi / 60
    elapsed_time = distance_rotated / output_speed_rad
    return elapsed_time
