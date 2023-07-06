# create a class (Fan)
class Fan:
# create a constructor contains the values needed
    def __init__(self, speed = 'Slow', radius = 5, color = 'Blue', power = 'off'):
        # create the variables applying encapsulation method
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__power = power
# Create def in all values (setters)
    # Speed
    def set_speed(self):
        if self.__speed == 1:
            self.__speed = 'Slow'
        elif self.__speed == 2:
            self.__speed = 'Medium'
        elif self.__speed == 3:
            self.__speed = 'Fast'
    # Radius
    def set_radius(self):
        return self.__radius
    # Color 
    def set_color(self):
        return self.__color
    # Power
    def set_power(self):
        if self.__power == 1:
            self.__power = 'ON'
        elif self.__power == 0:
            self.__power = "OFF"

# Returning all the variables from the setters
    # speed
    def get_speed(self):
        return self.__speed
    # radius
    def get_radius(self):
        return self.__radius
    # color 
    def get_color(self):
        return self.__color
    # power
    def get_power(self):
        return self.__power
