#check job number
def input_checker():
    valid=False
    while not valid:
        try:
            job_number = int(input("Enter a job number: "))
            if 0<=job_number:
                return job_number
            else:
                print("Please enter a valid number!")

        except ValueError:
            print("Please enter a valid number!")

#main routine
#run the number if it is valid
num=input_checker()
print("You entered {}".format(num))
