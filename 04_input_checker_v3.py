#check distance travelled
def input_checker():
    valid=False
    while not valid:
        try:
            distance_travelled = float(input("Enter a distance travelled (in km): "))
            if 0<=distance_travelled<=800:
                return distance_travelled
            elif distance_travelled<0:
                print("Please enter a valid number for distance!")
            else:
                print("Too far away! That seems impossible!")
        except ValueError:
            print("Please enter a valid number for distance!")

#main routine
#run the number if it is valid
distance=input_checker()
print("You entered {}km".format(distance))
