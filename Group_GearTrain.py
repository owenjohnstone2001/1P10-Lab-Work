''' IBEHS 1P10 Mini Milestone 12 Gear_Train class

Team Number: 76

Name: Owen Johnstone

Date: March 3, 2020 '''
class Gear_Train:
    def __init__(self,number_of_gears=2,gear_module=1):
        self.number_of_gears = number_of_gears
        self.gear_module = gear_module
        self.list_of_gear_teeth = [12]*number_of_gears
        self.gear_ratio = 1
        self.center_distance = 0
        self.output_speed = 0

    def get_gear_list(self):
        return self.list_of_gear_teeth

    def get_GR(self):
        return self.gear_ratio

    def get_CD(self):
        return self.center_distance

    def get_wo(self):
        return self.output_speed

    def get_gear_item(self, index):
        return self.list_of_gear_teeth[index]

    def set_gear_item(self, index_number, number_of_gear_teeth):
        self.list_of_gear_teeth[index_number] = number_of_gear_teeth

    def calc_GR(self):
        self.gear_ratio = self.list_of_gear_teeth[-1] / self.list_of_gear_teeth[0]
        return self.gear_ratio

    def calc_CD(self):
        for item in range (1, len(self.list_of_gear_teeth)-1):
            pitch_diameter = self.list_of_gear_teeth[item] * self.gear_module
            self.center_distance += pitch_diameter
        self.center_distance += ((self.list_of_gear_teeth[0] * self.gear_module) / 2) + ((self.list_of_gear_teeth[-1] * self.gear_module) / 2)
        return self.center_distance

    def calc_wo(self, input_speed):
        self.output_speed = input_speed / self.gear_ratio
        return self.output_speed 
