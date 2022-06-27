distance = float(input("Enter your distance travelled: "))
distance_travelled=round(distance)
#for testing purpose
print("rounded distance(km): ", distance_travelled)
if distance_travelled<=5:
    charge1=10
else:
    charge1=(distance_travelled - 5) * 0.5 + 10
#for testing purpose
print("charge1: $", charge1)
