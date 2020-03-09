'''
IBEHS 1P10 Mini Milestone 10 Main File

Team Number: 76

Name: Owen Johnstone

Date: Jan. 21, 2020
'''

""" GIVEN Functions """
import time

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

## This function reads data from a file to a list
## This is a repeat of Mini-Milestone 7 (Wk-11), Objective #3/4
def read_file(filename):
    IO_gears = []
    with open(filename) as gear_list:
        for line in gear_list:
            line = float(line.rstrip())
            IO_gears.append(line)
    return IO_gears

##Student ID: 400242374
def simulate_motion(input_speed, first_level, second_level):
    data_list=[]
    gear_ratio = calc_GR(first_level, second_level)
    for i in range (7):
        if i%2 == 0:
            data_list.append("OPEN \t" + str((calc_elapsed_time(input_speed, gear_ratio)*i)))
        else:
            data_list.append("CLOSED \t"+ str((calc_elapsed_time(input_speed, gear_ratio)*i)))
    return data_list

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

##Main Function
def main():
    input_speed = 200
    FL = [12, 16, 40]
    SL = [12, 13, 13, 20]
    gear_list = 'GearList-1.txt'
    gear_ratios = 'GearRatios-1.txt'
    IO_gears = read_file('GearList-1.txt')
    list_of_GR = read_file('GearRatios-1.txt')
    list_of_data = simulate_motion(input_speed, FL, SL)

    for item in list_of_data:
        print(item)
        time.sleep(calc_elapsed_time(input_speed, calc_GR(FL, SL)))
    
    for item in list_of_GR:
        data = find_gear_config(item, IO_gears)
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t', round(item, 3))
        
#Add function call here (main)
main()
