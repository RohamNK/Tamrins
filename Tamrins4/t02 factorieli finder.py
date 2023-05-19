num = int(input("Adad ra vared konid: "))
i = 1
while(num > 1):
    i += 1
    num /= i
if num == 1:
    print('HAST!')
else:
    print('nist...!')
