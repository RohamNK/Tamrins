import math

print("Tamrin 1: Calculator")
print("a:sum")
print("b:sub")
print("c:mult")
print("d:div")
print("e:square root")
print("f: sine")
print("g: cosine")
print("h:tangent")
print("i:cotangent")
print("j:factorial")
print("Please select your action: ")
op = input()

if op in ["a", "b", "c", "d"]:
    x = float(input("Please enter the first number: "))
    y = float(input("Please enter the second number: "))
else:
    x = float(input("Please enter the number: "))

if op == "a":
    result = x + y
elif op == "b":
    result = x - y
elif op == "c":
    result = x * y
elif op == "d":
    if y == 0:
        result = "Cannot divide by zero!"
    else:
        result = x / y
elif op == "e":
    if x < 0:
        result = "Negative numbers can't have square roots!"
    else:
        result = x ** (1 / 2)
elif op == "f":
    result = math.sin(x * math.pi/180)
elif op == "g":
    result = math.cos(x * math.pi/180)
elif op == "h":
    result = math.tan(x * math.pi/180)
elif op == "i":
    result = 1 / (math.tan(x * math.pi/180))
elif op == "j":
    if x < 0:
        result = "Factorial not defined for negative values!"
    else:
        result = math.factorial(int(x))

print(result)
