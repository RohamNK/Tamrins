import random
n = int(input("Che tedad adad tolid shavad?  "))
range_start = int(input("Hadaghale rej chand bashad?  "))
range_end = int(input("Hadeaksare rej chand bashad?  "))
if range_end - range_start < n:
    print("Renj dorost nist")
else:
    numbers = []
    while len(numbers) < n:
        num = random.randint(range_start, range_end)
        if num not in numbers:
            numbers.append(num)
    print(numbers)
