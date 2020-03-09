# Owen Johnstone 
# Date: November 5, 2019

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

def objective2(number_of_teeth, module):
    pitch_diameter= []
    for teeth in number_of_teeth:
        p_diameter= module*teeth
        pitch_diameter.append(p_diameter) 
    return (pitch_diameter)

def objective3(gear_diameter):
    total= 0
    middle_diameters= gear_diameter[1:-1]
    for diameter in middle_diameters:
        total= total+ diameter
    radius_input= gear_diameter[0]/2
    radius_output= gear_diameter[-1]/2
    center_distance= total+ radius_input+ radius_output
    return center_distance

def objective4():
    length = 36
    positions = []
    for angle in range(0, 100, 10):
        point = [-length * math.cos(math.radians(angle)), 36 - (length * math.sin(math.radians(angle)))]
        positions.append(point)
    return positions

def main():
    # Inputs for objectives
    first_level = [5,12,17,32,61]
    second_level = [2,6,34,37]
    num_teeth = [32,45,3,14,12]
    module = 1
    pitch_d = objective2(num_teeth, module)

    # Describes the output, and rounds it to 2 decimal places
    print("Objective 1 - Gear Ratio:\t" + str(round(objective1(first_level, second_level), 2)) + "\n")
    print("Objective 2 - Pitch Diameters:")

    # Loop through items in the returned list and counted the number of gears. The pitch diameter
    # is rounded to 3 decimal places for each gear and printed
    count = 1
    for item in objective2(num_teeth,module):
        print("Gear #" + str(count) + ":\t" + str(round(item,3)))
        count += 1

    # Describes the output, and rounds it to 2 decimal places
    print("\nObjective 3 - Center Distance:\t" + str(round(objective3(pitch_d), 2)))

    # Loops through items in the returned list. Each item is separated into x-y components, rounded
    # to 3 decimal places and printed
    print("\nObjective 4 - Forefinger tip position in 10 degree increments (x,y)")
    for item in objective4():
        print(str(round(item[0], 3)) + "\t" + str(round(item[1], 3)))

main()
