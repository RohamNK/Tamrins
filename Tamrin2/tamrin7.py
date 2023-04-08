n = int(input("Enter how many numbers you want in the Fibonacci series: "))

x = 0
y = 1

print(x)
print(y)

for Fibo in range(n-2):
    z = x + y
    x = y
    y = z
    print(z)