user_list = []
while True:
    user_input = input("Adad ra vared konid, ya baraye etmame kar, kalame tamoom ra tayp konid: ")
    if user_input == 'tamoom':
        break
    else:
        user_list.append(int(user_input))

unique_list = []
for num in user_list:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)
