num1 = int(input("Adade aval: "))
num2 = int(input("Adade dovom: "))
smaller = min(num1, num2)
bmm = 1
for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        bmm = i
print("BMM ", num1, "va", num2, "mishe", bmm)
