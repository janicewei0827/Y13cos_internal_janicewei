#check minutes spent
def input_checker():
    valid=False
    while not valid:
        try:
            minutes_spent = int(input("Enter your minutes spent: "))
            if 0<minutes_spent:
                return minutes_spent
            else:
                print("Please enter a valid whole number!")
        except ValueError:
            print("Please enter a valid whole number!")

#main routine
#run the number if it is valid
minutes=input_checker()
print("You entered {} minutes".format(minutes))

