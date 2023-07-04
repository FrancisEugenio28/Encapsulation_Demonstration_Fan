# create a class (Fan)
class Fan:
# create a constructor contains the values needed
    def __init__(self, speed = 'Slow', radius = 5, color = 'Blue', power = 'off'):
        # create the variables applying encapsulation method
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__power = power
# Create def in all values
    # Speed
    def set_speed(self):
        while True:
            try:
                speed_input = int(input('Set the speed of the fan (1 for Slow, 2 for Medium, 3 for Fast): '))
                if speed_input == 1:
                    self.__speed = 'Slow'
                    break
                elif speed_input == 2:
                    self.__speed = 'Medium'
                    break
                elif speed_input == 3:
                    self.__speed = 'Fast'
                    break
                else:
                    print('Invalid input, please try again.')
            except ValueError:
                print('Invalid input, please enter a number.')
    # Radius
    # Color 
    # Power
