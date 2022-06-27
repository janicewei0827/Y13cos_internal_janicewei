#round distance values with 0.5s
#fix the error in v1

import math

distance = float(input("Enter your distance travelled: "))
if distance % 0.5 == 0:
    distance_travelled=math.ceil(distance)
else:
    distance_travelled=round(distance)

#for testing purpose
print("rounded distance(km): ", distance_travelled)
if distance_travelled<=5:
    charge1=10
else:
    charge1=(distance_travelled - 5) * 0.5 + 10
#for testing purpose
print("charge1: $", charge1)
