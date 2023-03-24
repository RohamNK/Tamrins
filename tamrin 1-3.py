print("Welcome to the average calculator")
a = input("Please enter your name: ")
b = input("Please enter your last name: ")
c = float(input("please enter your first score: "))
d = float(input("please enter your second score: "))
e = float(input("please enter your third score: "))
average = (c + d + e)/3
if average >= 17:
    result = "has passed with GREAT scores!"
elif  17 > average >= 12:
    result = "has passed with normal scores."
elif average < 12:
    result = "has not reached the optimum average scores and has failed."
print (a, b, result)