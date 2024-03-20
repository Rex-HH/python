from car import Car

my_new_car = Car('audi', 'rs6', 2024)
print(my_new_car.get_long_name())

my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(13)
my_new_car.update_odometer(46)
my_new_car.read_odometer()

print("-" * 40)


my_used_car = Car('audi', 'rs4', 2018)
print(my_used_car.get_long_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
