import random as rd
# Rock, Paper, and Scissors Game.

#
# A basic rock, paper, scissors game with python..
# The users have only 3 rounds, and at the end of the third round,
# the user who had more wins will automatically be the winner.
#
#

rounds = 0
while rounds <= 2:
    # User input
    User_1 = input("Choose one (Rock, Paper, or Scissors): ").lower()

    # Selects any of the 3 items in the List and display it to the other user for transparency😂
    user_2 = rd.choice(["rock", "paper", "scissors"]).lower()

    # To confirm if the user input matches pre-defined ones(rock, paper, scissors)
    if User_1 not in user_2:
        print("Please select the right option")
        continue

    if User_1 == "rock" and user_2 == "scissors":
        print(f"Person selected: {user_2}")
        print("User_1 won")
        continue
    elif User_1 == "scissors" and user_2 == "paper":
        print(f"Person selected: {user_2}")
        print("User_1 won")
    elif User_1 == "paper" and user_2 == "rock":
        print(f"Person selected: {user_2}")
        print("User_1 won")
    elif user_2 == User_1:
        print(f"Person selected: {user_2}")
        print("tie")
    else:
        print("User 2 won")
        # print("User_2 Chose: ", user_2)
    rounds += 1
    print(rounds)
