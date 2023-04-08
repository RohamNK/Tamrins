import random
x = 0
pcnumber = random.randint(10, 40)
print ("welcome to guess number! please select a number: ")
for i in range(10):
    usernumber = int(input())
    if pcnumber == usernumber:
        x = x + 1
        print("Good Job! Number of tries =", x)
        break
    elif i == 9:
        print("You ran out of choices!")
        break
    elif pcnumber < usernumber:
         x = x + 1
         print("Go down!")
    elif pcnumber > usernumber:
        x = x + 1
        print("Go up!")