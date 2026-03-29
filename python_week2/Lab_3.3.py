movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "The Lord of the Rings: The Return of the King"]
user_movies = input("Enter a movie you have watched recently:")
if user_movies in movies:
    print("You have watched this movie!")
elif user_movies not in movies:
    print("I have watched some of this movie but not all of it!")
elif user_movies == "The Shawshank Redemption":
    print(True)
elif user_movies not in movies:
    print("I have watched this movie but it is not on the list!")

else: user_movies not in movies
print("You have not watched this movie yet!")


secret_number = 7
user_input = input("Enter Y if you would like to play: ")
if user_input == "Y":
    guess = int(input("Guess the number I am thinking aboutbetween 1 and 20:"))
if guess == secret_number: 
    print("Congratulations! You guessed the number!")
elif guess < secret_number:
    print("Too low! Try again.")
elif guess == (secret_number + 1) or guess == (secret_number - 1):
    print("So close! You're just one number away!")
elif abs(guess - secret_number) == 1:
    print("So close! You're just one number away!")
else: print("Sorry, that's not correct. The number I was thinking of was", secret_number)



