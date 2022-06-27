import math
#distance travelled, charge 1
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

#charge for virus protection
#1 is for being selected, 0 is not being selected
var0=int(input("If virus protection is selected (Enter '1' for yes; Enter '0' for no): "))
if var0==1:
    minutes_spent = int(input("Enter your minutes spent on virus protection: "))
    charge2=0.8 * minutes_spent
else:
    charge2=0
#for testing purpose
print("charge2: $", charge2)

#charge for wof and tune
#1 is for being selected, 0 is not being selected
var1=int(input("If wof and tune is selected (Enter '1' for yes; Enter '0' for no): "))
if var1==1:
    charge3=100
else:
    charge3=0
#for testing purpose
print("charge3: $", charge3)

job_charge=charge1+charge2+charge3
#for testing purpose
print("Job charge: $",job_charge)
