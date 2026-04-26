import play_game
import utils

def game_menu():
    while True:
        print("\n--- Stone Paper Scissors ---")
        print("1. Play Game")
        print("2. Show Score")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            play_game.play()
        elif choice == "2":
            utils.show_score()
        elif choice == "3":
            print("Exiting game...")
            break
        else:
            print("Invalid choice!")

game_menu()
