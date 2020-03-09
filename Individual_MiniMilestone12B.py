''' IBEHS 1P10 Mini Milestone 12B Individual File
Name: Owen Johnstone

Date: March 3, 2020 '''
from Team76_GearTrain import *

##Student ID: 400268572
def create_mechanism_B(input_speed, num_gear_trains):
    total_gear_ratio = 1
    for i in range(0,num_gear_trains):
        num_gears = int(input("Please enter the number of gears: "))
        module = int(input("Please enter the module: "))
        gear_train = Gear_Train(num_gears, module)
        for i in range(0, num_gears):
            num_teeth = int(input("Please enter the number of teeth: "))
            gear_train.set_gear_item(i, num_teeth)
        total_gear_ratio = total_gear_ratio * gear_train.calc_GR()
        input_speed = gear_train.calc_wo(input_speed)
    return total_gear_ratio, input_speed

def main():
    inp_speed = int(input("Please enter the input speed: "))
    num_gear_trains = int(input("Please enter the number of gear trains: "))
    gear_ratio, output_speed = create_mechanism_B(inp_speed, num_gear_trains)
    print("Gear ratio: " + str(round(gear_ratio, 2)) + "\tOutput speed: " + str(round(output_speed, 2)))

main()
