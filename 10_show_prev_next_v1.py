#get data from user and store it in a list, then
#display the most recent job information nicely

#set up empty lists
job_numbers = [5, 4, 3, 2, 1]
current_index = 0

#get information

seq = ""

print("*** The Full Lists ***")
print("Job numbers: ", job_numbers)
print()
print("*** The Most Recent Job Information ***")
print("job number: ", job_numbers[current_index])
print()

while seq != "xxx":
    seq = input("Enter 'prev' to view the previous job, or 'next' to view the next job: ")

    if seq == "xxx":
        break
    elif seq == 'prev':
        current_index -= 1
        print("job number: ", job_numbers[current_index])
    elif seq == 'next':
        current_index += 1
        print("job number: ", job_numbers[current_index])
    else:
        seq=input("Invalid input, enter again: ")
