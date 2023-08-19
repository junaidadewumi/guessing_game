"""
Assignment
Create a guessing game, user have access to 3 attempts  to enter any number between 0 and 9 after which the game will end,
if the user entered the right number, the user win the game.
"""


# #solution
guess_count = 0
right_number = 5
while guess_count < 3:
    user = int(input("Enter your guess: "))
    if user == right_number:
        print("You won")
        break
    else:
        print("You are wrong")
    guess_count += 1
else:
    print("Game over")