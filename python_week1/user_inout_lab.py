# Exercise 1 – Basic Input
name = input("Enter your name: ")
print(name)

# Exercise 2 – Input with Prompt
city = input("Which city do you live in? ")
print(city)

# Exercise 3 – Numeric Input Without Conversion
age = input("Enter your age: ")
try:
    result = age + 5
except TypeError as e:
    print(f"TypeError: {e}")

# Exercise 4 – Convert to int
age = int(input("Enter your age: "))
print(age)

# Exercise 5 – Future Age Calculation
print(age + 10)

# Exercise 6 – Float Input
price = float(input("Enter price: "))
print(price)

# Exercise 7 – Price with 17% Tax
total = price * 1.17
print(total)

# Exercise 8 – F-String with Tax
print(f"The final price is {total}")

# Exercise 9 – Two Decimal Places
print(f"The final price is {total:.2f}")

# Exercise 10 – Sum of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)

# Exercise 11 – Average of Three Numbers
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
average = (n1 + n2 + n3) / 3
print(average)

# Exercise 12 – Square Feet to Square Meters
sqft = float(input("Enter house size in square feet: "))
sqm = sqft / 10.764
print(sqm)

# Exercise 13 – F-String with Conversion
print(f"{sqft} square feet is equal to {sqm} square meters")

# Exercise 14 – Formatted Output
print(f"{sqft:.0f} square feet is equal to {sqm:.2f} square meters")

# Exercise 15 – Full Program
size = float(input("Enter house size in square feet: "))
converted = size / 10.764
print(f"{size:.0f} square feet is equal to {converted:.2f} square meters")