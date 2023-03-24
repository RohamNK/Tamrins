print("Welcome to my triangle validator!")

a = float(input("Please enter the first side lenght: "))
b = float(input("Please enter the second side lenght: "))
c = float(input("Please enter the third side lenght: "))
if a < 0 or b < 0 or c < 0:
    result = "sides cannot be negative!"
elif a == 0 or b == 0 or c == 0:
    result = "sides cannot be zero!"
elif a + b > c or a + c > b or b + c > a:
    result = "triangle sides are valid!"
print (result)