# def hello():
#     print("Hello")
# print("start")
# hello()
# print("end")

# def user_age_in_seconds():
#     age = int(input("What is your age: "))
#     age_seconds = age * 365 * 24 * 60 * 60
#     print(f"Your age in seconds is: {age_seconds}")
# user_age_in_seconds()

# Scopes
# friends = ["John", "Jane"]

# def add_friend():
#     friend_name = input("Enter your friend name: ")
#     friends = friends + [friend_name]

# add_friend()

# print(friends)

friends = []

def add_friends():
    friends.append(input("Enter whatever their name is: "))

add_friends()
print(friends)

add_friends()
add_friends()
print(friends)
