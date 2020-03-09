'''
IBEHS 1P10 Mini Milestone 10 Individual File
Name: Owen Johnstone

Date: Jan. 21, 2020
'''

""" GIVEN Functions """
## This function calculates the gear ratio of your gearing mechanism
## This is a repeat of Mini-Milestone 5 (Wk-8), Objective #1
def calc_GR(gear_list1, gear_list2):
    ratio1 = gear_list1[-1] / gear_list1[0]
    ratio2 = gear_list2[-1] / gear_list2[0]
    gear_ratio = ratio1 * ratio2
    return gear_ratio

## This function calculates the required time (in seconds) to rotate the forefinger 90°
## This is a repeat of Mini-Milestone 4 (Wk-6&7), combining Objective #2 and Objective #4
def calc_elapsed_time(input_speed, gear_ratio):
    FOREFINGER_ROTATION_ANGLE = 90
    num_finger_revolutions = FOREFINGER_ROTATION_ANGLE / 360
    num_motor_revolutions = gear_ratio * num_finger_revolutions
    rev_per_sec = input_speed / 60
    elapsed_time = num_motor_revolutions / rev_per_sec
    return elapsed_time

##Student ID: 400268572
def find_gear_config(gear_ratio, gear_teeth):
    first_level_input = 12
    second_level_input = 12
    data = []
    for i in gear_teeth:
        for j in gear_teeth:
            calculated_gear_ratio = round((i / first_level_input) * (j / second_level_input), 3)
            if calculated_gear_ratio == round(gear_ratio, 3):
                return [12, i, 12, j]

##Do not include any function calls - as they will be called in main()

