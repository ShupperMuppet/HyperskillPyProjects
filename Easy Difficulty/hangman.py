# Write your code here
import random

possible_answers = ['python', 'java', 'kotlin', 'javascript']

print("H A N G M A N")
while True:
    option = input("Type \"play\" to play the game, \"exit\" to quit: ")

    if option == "exit":
        exit(0)

    elif option == "play":
        print()
        word = random.choice(possible_answers)
        typed_letters = []
        win = False
        hint = '-'
        for _ in range(len(word) - 1):
            hint += '-'
        count = 8
        while count > 0:
            print(hint)

            letter = input("Input a letter: ")

            if not (len(letter) == 1):
                print("You should print a single letter")

            elif not letter.islower():
                print("It is not an ASCII lowercase letter")

            elif letter in typed_letters:
                print("You already typed this letter")

            elif letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        hint = hint[:i] + letter + hint[i+1:]

            else:
                print("No such letter in the word")
                count -= 1

            if word == hint:
                win = True
                break

            if count:
                print()

            if letter not in typed_letters:
                typed_letters.append(letter)


        if win:
            print(f"You guessed the word {word}!")
            print("You survived!")
        else:
            print('You are hanged!')
