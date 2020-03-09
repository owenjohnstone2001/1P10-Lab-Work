'''
IBEHS 1P10 Mini Milestone 11 Main File

Team Number: 76

Name: Owen Johnstone

Date: Feb. 25, 2020
'''
import matplotlib.patches as patches
import math
import matplotlib.pyplot as plt

""" GIVEN Functions """
## This function creates 6" x 6" graphics window
## The functional workspace is created within this window
def functional_workspace():
    fig, ax = plt.subplots(1,1,figsize=(6,6))
    rect = patches.Rectangle((-15,-15),30,30,angle=0.0,fill = False, ls = '--', color = 'r',linewidth=1.5)
    ax.add_patch(rect)
    plt.xlim((-45,45))
    plt.ylim((-45,45))
    ax.set(title='Forefinger-Thumb Path',
            xlabel = 'X (mm) ',
            ylabel = 'Y (mm) ')

##Student ID: 400242374
def forefinger_position(degree_of_increments):
    forefinger_length= 36
    position_list= []

    for angle in range(0, 91, int(degree_of_increments)):
        xcoordinates= -(forefinger_length*math.cos(math.radians(angle)))
        ycoordinates= 36 - forefinger_length*math.sin(math.radians(angle))
        position_list.append([xcoordinates, ycoordinates])
    return position_list

##Student ID: 400268572
def thumb_position(num_inc):
    thumb_length = 42
    coordinate_list = []
    
    for angle in range(0,91,int(num_inc)):
        x_coordinate = 42 - thumb_length * math.sin(math.radians(angle))
        y_coordinate = -thumb_length * math.cos(math.radians(angle))
        coordinate_list.append([x_coordinate, y_coordinate])
        
    return coordinate_list

##Student ID: 400242374
def write_lists(file_name, list1, list2):
    length_of_list1= float(len(list1))
    length_of_list2= float(len(list2))
    if length_of_list1 == length_of_list2:
        with open(file_name, "w") as file:
            for i in range(len(list1)):
                file.write(str(list1[i])+"\t"+str(list2[i])+"\n")
    else:
        print("The lengths of the two lists are not equal.")

##Student ID: 400268572
def append_array(text_file, data_array):
    with open(text_file, 'a') as txt:
        for item in data_array:
            txt.write(str(item[0]) + '\t' + str(item[1]) + '\n')

##Student ID: 400242374
def plot_forefinger():
    number_of_increments=int(input("Enter a value for the number of increments."))
    while 90 % number_of_increments != 0:
        print("The number you enetered is not go into 90 evenly. Try another number.")
        number_of_increments= int(input("Enter a value for the number of increments."))

    functional_workspace()
    data_list= forefinger_position(number_of_increments)
    for element in range(len(data_list)):
        x_cd= data_list[element][0]
        y_cd= data_list[element][1]
        plt.scatter(x_cd,y_cd)
    plt.show()

##Student ID: 400268572
def plot_thumb():
    num_inc = int(input('Enter the number of degrees to increment by: '))

    while 90 % num_inc != 0:
        print('Please enter a number of degrees that evenly divides into 90.')
        num_inc = int(input('Enter the number of degrees to increment by: '))

    functional_workspace()
    data_list = thumb_position(num_inc)
    
    for i in range(len(data_list)):
        x_cd = data_list[i][0]
        y_cd = data_list[i][1]
        
        plt.scatter(x_cd, y_cd, c='r')
    plt.show()

##Main Function
def main():
    inc_num = int(input('Please enter the number of degrees to increment by: '))
    
    while 90 % inc_num != 0:
        print('Please enter a number of degrees that evenly divides into 90.')
        inc_num = int(input('Enter the number of degrees to increment by: '))
        
    functional_workspace()
    thumb_pos  = thumb_position(inc_num)
    finger_pos = forefinger_position(inc_num)

    thumb_x_list = []
    forefinger_x_list = []

    thumb_y_list = []
    forefinger_y_list = []

    for i in range(len(thumb_pos)):
        thumb_x = thumb_pos[i][0]
        thumb_x_list.append(round(thumb_x, 2))
        
        thumb_y = thumb_pos[i][1]
        thumb_y_list.append(round(thumb_y, 2))

        finger_x = finger_pos[i][0]
        forefinger_x_list.append(round(finger_x, 2))
        
        finger_y = finger_pos[i][1]
        forefinger_y_list.append(round(finger_y, 2))

        plt.scatter(thumb_x, thumb_y)
        plt.scatter(finger_x, finger_y)

    
    plt.show()

    x_coordinates = thumb_x_list + forefinger_x_list
    y_coordinates = thumb_y_list + forefinger_y_list

    write_lists('Objective3.txt', x_coordinates, y_coordinates)
    append_array('Objective4.txt', finger_pos)
    append_array('Objective4.txt', thumb_pos)

main()
