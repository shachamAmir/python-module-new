def add(x, y): 
    pass
    print(x + y)

add(5, 6)
add(5, 10)
add(5, 15)
add(9, 8)
add(0, 3)
def say_hello(name):
    print(f"Hello, {name}!")
say_hello("Alice")
say_hello("Bob")
say_hello("Charlie") 


def big_hello(name, age):
    print(f"Hello, {name}! You are {age} years old.")
# Keyword arguments
user_name = input("your name:")
user_age = int(input("your age:"))
big_hello(name=user_name, age=user_age)
