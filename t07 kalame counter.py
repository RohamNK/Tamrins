sentence = input('lotfan jomle khod ra vared konid: ')
word_count = 0
in_word = False
for char in sentence:
    if char != ' ' and not in_word:
        in_word = True
        word_count += 1
    elif char == ' ' and in_word:
        in_word = False
print('tedad kalimat: ', word_count)
