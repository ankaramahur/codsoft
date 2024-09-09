import random

while True:
    user = input("Enter a choice (rock, paper, scissors): ")
    possibilities = ["rock", "paper", "scissors"]
    computer = random.choice(possibilities)
    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print(f"rock vs scissors -> scissors wins")
        else:
            print("rock vs paper -> paper wins")
    elif user == "paper":
        if computer == "rock":
            print("paper vs rock -> paper wins")
        else:
            print("paper vs scissors -> scissors wins")
    elif user == "scissors":
        if computer == "paper":
            print("scissors vs paper -> scissors wins")
        else:
            print("rock vs scissors -> scissors wins")

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
