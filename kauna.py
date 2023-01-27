import time

class_start_time = "9:00 AM" # set the class start time

student_name = input("What is your name? ")
student_arrival_time = input("What time did you arrive to class? (Format: HH:MM AM/PM) ")

# convert class start time and student arrival time to seconds
class_start_time_seconds = time.mktime(time.strptime(class_start_time, "%I:%M"))
student_arrival_time_seconds = time.mktime(time.strptime(student_arrival_time, "%I:%M"))

# calculate the difference in seconds between the two times
time_difference = student_arrival_time_seconds - class_start_time_seconds

# check if the student is early, on time, or late
if time_difference < 0:
    print(student_name + " is early to class by " + str(abs(time_difference)) + " seconds.")
elif time_difference == 0:
    print(student_name + " is on time to class.")
else:
    print(student_name + " is late to class by " + str(time_difference) + " seconds.")