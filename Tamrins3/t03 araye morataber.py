numbers = [float(input("Adade aval ra vared konid: "))]
while True:
    num = input("adade badi ra vared kondi (ya baraye khateme benevisid END): ")
    if num == 'END':
        break
    numbers.append(float(num))
is_ordered = True
for i in range(len(numbers) - 1):
    if not (numbers[i] <= numbers[i + 1] or numbers[i] >= numbers[i + 1]):
        is_ordered = False
        break
if is_ordered:
    print("Adad ha tartibe dorosti darand.")
else:
    print("Adadha be ham rikhte hastand.")
