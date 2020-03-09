'''
IBEHS 1P10 Mini Milestone 7 Individual File
Name: Owen Johnstone

Date: Nov. 26, 2019
'''

""" GIVEN Functions """

## This function calculates the gear ratio of your gearing mechanism
def calc_GR(gear_list1, gear_list2):
    ratio1 = gear_list1[-1] / gear_list1[0]
    ratio2 = gear_list2[-1] / gear_list2[0]
    gear_ratio = ratio1 * ratio2
    return gear_ratio

## This function calculates the pitch diameter (in mm) for a set of gears
def calc_PD(gear_list, module):
    pitch_diameter_list = []
    for gear in gear_list:
        pitch_diameter_list.append(gear * module)
    return pitch_diameter_list

## This function calculates the center distance (in mm) between input and output for a set of gears
def calc_CD(pitch_diameter_list):
    center_distance = 0
    for gear in pitch_diameter_list:
        center_distance += gear
    center_distance -= (pitch_diameter_list[0])/2
    center_distance -= (pitch_diameter_list[len(pitch_diameter_list)-1])/2
    return center_distance



##Student ID: 400268572
def verify_gear_ratio(g_ratio, f_level, forefinger_sl, thumb_sl):
    finger_gear_ratio = calc_GR(f_level, forefinger_sl)
    thumb_gear_ratio = calc_GR(f_level, thumb_sl)
    if finger_gear_ratio == g_ratio and thumb_gear_ratio == g_ratio:
        print("Both motor-to-forefinger and motor-to-thumb gear ratios match.")
    elif finger_gear_ratio == g_ratio and thumb_gear_ratio != g_ratio:
        print("Only the motor-to-finger gear ratio matches.")
    elif finger_gear_ratio != g_ratio and thumb_gear_ratio == g_ratio:
        print("Only the motor-to-thumb gear ratio matches.")
    elif finger_gear_ratio != g_ratio and thumb_gear_ratio != g_ratio:
        print("Neither gear ratios match.")

def read_file_case2(file_name):
    with open(file_name,'r') as my_file:
        data = my_file.read()
        data = data.split()
        int_data = []
        for item in data:
            int_data.append(int(item))
        return int_data

def gear_occurence():
    text_file = input("Please input the name of the desired text file: ")
    given_gear_list = read_file_case2(text_file)
    gear_teeth = int(input("Please input the number of gear teeth: "))
    count = 0
    for item in given_gear_list:
        if item == gear_teeth:
            count += 1
    print("There were " + str(count) + " gear(s) in the file with " + str(gear_teeth) + " teeth.")
    
    
