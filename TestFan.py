from Fan import Fan
# create 2 fan
fan1 = Fan(3, 10, 'Yellow', 1)
fan2 = Fan(2, 5, 'Blue', 0)
# fan1 assign all attributes and print all the attributes
fan1_attribute = print("Speed: ", fan1.get_speed(), "\nRadius: ", fan1.get_radius(), "\nColor: ", fan1.get_color(), "\nPower: ", fan1.get_power())
# fan2 assign all attributes and print all the attributes
fan2_attribute = print("Speed: ", fan2.get_speed(), "\nRadius: ", fan2.get_radius(), "\nColor: ", fan2.get_color(), "\nPower: ", fan2.get_power())