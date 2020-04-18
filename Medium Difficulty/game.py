import random

weakness = {"paper": "scissors", "rock": "paper", "scissors": "rock"}
moves = ["paper", "scissors", "rock"]
rating = 0
name = input("Enter your name: ")
print(f"Hello, {name}")

# Getting Userscore
with open("rating.txt", "r") as f:
    for line in f:
        if name in line:
            rating = int(line.split()[1])

# Get Options
opt = input()
if opt:
    words = opt.split(',')
    moves = words
    length = len(words)
    att_count = length // 2
    weakness = {}
    count = 0
    while count < length:
        weakness[words[count]] = words[count + 1:count + att_count + 1]
        if len(weakness[words[count]]) < att_count:
            missing = att_count - len(weakness[words[count]])
            for word in words[0:missing]:
                weakness[words[count]].append(word)
        count += 1

print("Okay, let's start")
while True:
    user_choice = input()
    comp_choice = random.choice(moves)

    if user_choice == "!exit":
        print("Bye!")
        exit(0)
    elif user_choice == "!rating":
        print(f"Your rating: {rating}")
    elif user_choice not in moves:
        print("Invalid input")
    elif user_choice == comp_choice:
        print(f"There is a draw ({comp_choice})")
        rating += 50
    elif comp_choice in weakness[user_choice]:
        print(f"Sorry, but computer chose {comp_choice}")
    else:
        print(f"Well done. Computer chose {comp_choice} and failed")
        rating += 100
