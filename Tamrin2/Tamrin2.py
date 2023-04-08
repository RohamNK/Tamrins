import random

usscore = 0
pcscore = 0
print("Welcome to the game!")
while pcscore < 5 and usscore < 5:
    x = random.randint(1, 3)
    if x == 1:
        pcchoice = "rock"
    elif x == 2:
        pcchoice = "paper"
    elif x == 3:
        pcchoice = "scissors" 
   
    uschoice = input("Enter your choice: rock, paper, or scissors. ")
    if uschoice not in ["rock", "paper", "scissors"]:
        print("you have to select an option!")
    else:
        print("💻", pcchoice)
        print("👤", uschoice)
    if pcchoice == "rock" and uschoice == "paper":
        usscore = usscore + 1
    elif pcchoice == "rock" and uschoice == "scissors":
        pcscore = pcscore + 1
    elif pcchoice == "paper" and uschoice == "rock":
        pcscore = pcscore + 1
    elif pcchoice == "paper" and uschoice == "scissors":
        usscore = usscore + 1
    elif pcchoice == "scissors" and uschoice == "rock":
        usscore = usscore + 1
    elif pcchoice == "scissors" and uschoice == "paper":
        pcscore = pcscore + 1

print("Final score:")
print("USER:", usscore)
print("PC:", pcscore)
if pcscore > usscore:
    print("Computer wins!")
elif usscore > pcscore:
    print("You win!")
else:
    print("Tie!")