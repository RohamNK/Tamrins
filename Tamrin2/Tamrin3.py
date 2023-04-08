print("Welcome to the mean calculator! Please enter a score:")
x = 1
total_score = float(input())

print("Good, now enter another score:")
total_score = total_score + float(input())
x = x + 1

while True:
    print("Good. Now choose an option: a = enter another score, or b = see the results")
    op = input()
    
    if op == "a":
        score = input("Enter a score, or enter 'exit' to see the results: ")
        if score == "exit":
            print("Final mean:", total_score / x)
            break
        else:
            total_score = total_score + float(score)
            x = x + 1
            print("Score was recorded. Please enter another score; else, enter 'exit' to see the final result.")
    elif op == "b":
        print("Final mean:", total_score / x)
        break
    else:
        print("Invalid input. Please enter 'a' or 'b'.")
