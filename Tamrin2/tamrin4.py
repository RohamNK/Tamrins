print("Convert time to seconds!") 

print("Please enter the hours, minutes, and seconds.")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))
print("Your input is:", hours, ":", minutes, ":", seconds)
total_seconds = hours * 3600 + minutes * 60 + seconds

print("Total seconds:", total_seconds)
