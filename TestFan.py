# import our code 
from Fan import Fan
# create 2 fan for testing
fan1 = Fan()
fan2 = Fan()
# call all the functions in fan1
fan1.set_speed()
fan1.set_radius()
fan1.set_color()
fan1.set_power()
# print the output
print('\n[Fan number 1] \nSpeed: ', fan1.get_speed(), '\nRadius: ', fan1.get_radius(), '\nColor: ', fan1.get_color(), '\nPower: ', fan1.get_power())
# call all the functions in fan2
# print the output