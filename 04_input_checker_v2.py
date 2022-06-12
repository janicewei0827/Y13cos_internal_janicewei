#check customer name
def input_checker():
    valid=False
    while not valid:
        customer_name = input("Enter a customer name: ")
        if len(customer_name)== 0 or customer_name.isspace():
            print("Please enter a valid name!")
        else:
            return customer_name



#main routine
#run the number if it is valid
name=input_checker()
print("You entered {}".format(name))
