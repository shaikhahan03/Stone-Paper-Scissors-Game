import random
import result
import utils

def play():
    options = ["stone", "paper", "scissors"]

    user_choice = input("Enter stone, paper, or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice!")
        return

    computer_choice = random.choice(options)

    print("Computer chose:", computer_choice)

    winner = result.check_winner(user_choice, computer_choice)

    if winner == "user":
        print("You win!")
        utils.user_score += 1
    elif winner == "computer":
        print("Computer wins!")
        utils.computer_score += 1
    else:
        print("It's a draw!")
