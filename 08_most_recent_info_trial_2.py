#get data from user and store it in a list, then
#display the most recent job information nicely

#set up empty lists
job_numbers=[]
names=[]
charges=[]

#get information
get_job_num=""
get_name=""
get_charge=""

while get_job_num != "xxx":
    get_job_num=input("Enter your job number: ")

    if get_job_num == "xxx":
        break
    else:
        get_name=input("Enter your name: ")
        #this will not be entered bu user in the GUI
        get_charge=input("Enter your job charge: ")
        print()

    job_numbers.insert(0, get_job_num)
    names.insert(0, get_name)
    charges.insert(0, get_charge)
    current_index=0

if len(job_numbers) == 0 or len(names) == 0 or len(charges) == 0:
    print("OOps - the lists are empty")

else:
    print()
    print("*** The Full Lists ***")
    print("Job numbers: ", job_numbers)
    print("Customer names: ", names)
    print("Job charges: ", charges)
    print()
    print("*** The Most Recent Job Information ***")
    print("job number: ", job_numbers[current_index])
    print("customer name: ", names[current_index])
    print("job charge: ", charges[current_index])
