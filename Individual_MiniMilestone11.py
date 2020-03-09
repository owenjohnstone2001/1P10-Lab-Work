'''
IBEHS 1P10 Mini Milestone 11 Individual File
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

##Student ID: 400268572
def thumb_position(num_inc):
    thumb_length = 42
    coordinate_list = []
    
    for angle in range(0,91,int(num_inc)):
        x_coordinate = 42 - thumb_length * math.sin(math.radians(angle))
        y_coordinate = -thumb_length * math.cos(math.radians(angle))
        coordinate_list.append([x_coordinate, y_coordinate])
        
    return coordinate_list

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

def append_array(text_file, data_array):
    with open(text_file, 'a') as txt:
        for item in data_array:
            txt.write(str(item[0]) + '\t' + str(item[1]) + '\n')
