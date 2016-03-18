import test3_packages.lists
print(test3_packages.lists.car_list)

from test3_packages import lists
print(lists.car_list)

from test3_packages.lists import car_list
print(car_list)

from test3_packages.lists import car_list as coches
print(coches)

from test3_packages.lists import *
print(car_list)