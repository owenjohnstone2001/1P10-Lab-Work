import math

def objective1(inputspeed, gearratio):
    outputspeed= inputspeed/gearratio
    return outputspeed

def objective2(gear_ratio):
    finger_rev= 90/360
    input_rotations= finger_rev*gear_ratio
    return input_rotations

def objective3 (angle):
    x_coor= -36*math.cos(angle)
    y_coor= 36- 36*math.sin(angle)
    return [x_coor, y_coor]

def objective4(inp_speed, gear_ratio):
    distance_rotated= 90*math.pi/180
    output_speed_rpm= inp_speed/gear_ratio
    output_speed_rad= output_speed_rpm*2*math.pi/60
    elapsed_time= distance_rotated/output_speed_rad
    return elapsed_time

def main():
    gearratio= 50/9
    inputspeed= 200
    angle= 60
    #described what the output is and rounded the answer to two decimal places, and then concatenated the answer with the strings
    print("The output speed is\t" + str(round(objective1(inputspeed, gearratio),2)) + " rpm")
    #described what the number of revolutions is and rounded the answer to two decimal places, and then concatenated the answer with the strings
    print("The number of motor revolutions per 90 degree forfinger rotation is\t" + str(round(objective2(gearratio),2)) + " revolutions")
    #retrived the first item of the list outputted by objective3 and rounded it to two deciaml places, the smae was repeated with the second item, and then both values were made into a list
    print("The x-y coordinate points of the forefinger tip for a given angle of forefinger rotation are\t"+ str([round(objective3(angle)[0],2), round(objective3(angle)[1],2)]))
    #described what the elapsed time is and rounded the answer to two decimal places, and then concatenated the answer with the strings
    print("The elapsed time to close forfinger is\t" + str(round(objective4(inputspeed, gearratio),2)) + " seconds")
    
main()
    
