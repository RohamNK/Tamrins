import random

wb = ["salam", "invari", "oonvari", "kotlet", "hamsayeh", "havadar", "mashin", "mahsa", "mojarad", "mihan", "kafsh", "dastgah", "santoor", "kabab", "hasan", "dohol", "pashmak", "moz", "nargil", "metro", "kafshdoozak", "internet", "soozan", "roshan", "masjed", "sabzipolo", "baghalipolo", "dokhtar", "pesar", "sandis"]

usmistakes = 0
goodch = []
badch = []

x = random.randint(0, len(wb)-1)
word = wb[x]
while usmistakes < 6:
    for i in range(len(word)):
        if word[i] in goodch:
            print(word[i], end="")
        else:
            print("_ ", end="")
    if all(letter.lower() in goodch for letter in word):
        print("\nBordi!")
        break
    userchar = input("\nPlease write your guess: ").lower()
    if len(userchar) == 1:
        if userchar in goodch or userchar in badch:
            print("You've already guessed that character!")
        elif userchar in word.lower():
            goodch.append(userchar)
            print("✅")
        else:
            badch.append(userchar)
            usmistakes += 1
            print("❌")
    else:
        print("Invalid character!")
if usmistakes == 6:
    print("\nR.I.P!!!")
    print("Javab:", word)
