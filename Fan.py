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
        while True:
            try:
                self.__speed = int(input('Set the speed of the fan (1 for Slow, 2 for Medium, 3 for Fast): '))
                if self.__speed == 1:
                    self.__speed = 'Slow'
                    break
                elif self.__speed == 2:
                    self.__speed = 'Medium'
                    break
                elif self.__speed == 3:
                    self.__speed = 'Fast'
                    break
                else:
                    print('Invalid input, please try again.')
            except ValueError:
                print('Invalid input, please enter a number.')
    # Radius
    def set_radius(self):
        self.__radius = int(input('Set the radius of the fan: '))
    # Color 
    def set_color(self):
        self.__color = str(input('Please describe the color of the Fan: '))
    # Power
    def set_power(self):
        while True:
            try:
                self.__power = int(input('(0 if you want to turn off the fan, 1 if you want to turn on the fan) | 1 | 0 |: '))
                if self.__power == 1:
                    self.__power = 'ON'
                    break
                elif self.__power == 0:
                    self.__power = "OFF"
                    break
                else:
                    print('Invalid input, please try again.')
            except ValueError:
                print('Invalid input, please enter a number.')

# Returning all the variables from the setters
    # speed
    def get_speed(self):
        return str(self.__speed)
    # radius
    def get_radius(self):
        return self.__radius
    # color 
    def get_color(self):
        return self.__color
    # power
    def get_power(self):
        return str(self.__power)
