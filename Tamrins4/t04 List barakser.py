user_list = []
while True:
    user_input = input("Adad ra vared konid, ya baraye etmame kar, kalame tamoom ra tayp konid: ")
    if user_input == 'tamoom':
        break
    else:
        user_list.append(int(user_input))

reversed_list = []
while user_list:
    last_element = user_list.pop()
    reversed_list.append(last_element)

print(reversed_list, end="")
