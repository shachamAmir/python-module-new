# The Boolean data type has only twp availanle values: 
# True and False. 
# These values are used to represent the truth value of an expression. 
# In Python, the Boolean data type is represented by the bool class.

# Example of Boolean values:
is_raining = True
print(type(is_raining))  # Output: <class 'bool'>
print(is_raining)  # Output: True
is_sunny = False
print(type(is_sunny))  # Output: <class 'bool'>
print(is_sunny)  # Output: False
# Boolean values can be used in conditional statements to control the flow of a program.
if is_raining:
    print("Don't forget to take an umbrella!")
else:    print("Enjoy the sunny weather!")
# Output: Don't forget to take an umbrella!
# Boolean values can also be used in logical operations such as AND, OR, and NOT.
is_weekend = True
is_holiday = False
if is_weekend and is_holiday:
    print("It's a perfect day for relaxation!")
elif is_weekend or is_holiday:
    print("It's a good day to take a break!")
else:    print("It's a regular workday.")
# Output: It's a good day to take a break!
# In Python, the following values are considered False in a Boolean context:
# - None
# - False
# - 0 (zero of any numeric type)
# - 0.0 (zero float)
# - 0j (zero complex)
# - Empty sequences and collections (e.g., '', [], {}, set())
# All other values are considered True in a Boolean context.
# Example of values considered False:
print(bool(None))  # Output: False
print(bool(0))  # Output: False
print(bool(""))  # Output: False
print(bool([]))  # Output: False
print(bool({}))  # Output: False
print(bool(set()))  # Output: False
# Example of values considered True:
print(bool(1))  # Output: True
print(bool(-1))  # Output: True
print(bool("Hello"))  # Output: True
print(bool([1, 2, 3]))  # Output: True
print(bool({'key': 'value'}))  # Output: True
print(bool({1, 2, 3}))  # Output: True  

# Comparison operators
print(5 == 5)  # Output: True
print("baba" == "baba")  # Output: True
print(5 > 3)  # Output: True
print(5 < 3)  # Output: False 
print(10 != 8)  # Output: True
print(10 != 10)  # Output: False

# comparing lists
friends = ["Bob", "Rolf", "Anne"]
abroad = ["Bob", "Anne", "Rolf"]

print(set(friends) == set(abroad))

# "==" or "is"
print(friends[1] is abroad[2])

s = {(5+5+5+5+5) / 5 == 5}
print(s)  # Output: {True} 

