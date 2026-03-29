friends = ["Arthur", "Thomas", "John"]
print(("Finn") in friends)

movies = ["The Matrix", "Immortal man", "Inception"]   # add more movies
user_movie = input("Enter a movie you have watched recently: ")
print("rix" in "The Matrix")

print(user_movie in movies)

if user_movie in movies:
    print("You have watched this movie!")
else:    print("You have not watched this movie yet!")

if user_movie in movies:
    print(" This movie is in the list!")
else:
    print("This movie is not in the list!")
