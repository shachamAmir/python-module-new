# while loops basics
# user_inputb = input("Would you like to continue? (y/n) ")

# while user_inputb != "n":
#     print("game is running")
#     user_inputb = input("Would you like to play again? (y/n) ")

while True: 
    user_input = input("Would you like to play? (y/n)")

    if user_input == "n":
        break
    print("game is running")
    