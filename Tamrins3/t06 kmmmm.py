num1 = int(input("Adade aval: "))
num2 = int(input("Adade dovom: "))
greater = max(num1, num2)
for kmm in range(greater, num1 * num2 + 1, greater):
    if kmm % num1 == 0 and kmm % num2 == 0:
        break
print("KMM", num1, "va", num2, "mishe", kmm)
