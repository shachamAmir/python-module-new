# Exercise 1 - sum, count, average
# def list_stats(numbers):
#     total = sum(numbers)
#     count = len(numbers)
# #     average = total / count
#     return (total, count, average)

# print(list_stats([1, 2, 3, 4, 5]))

# def my_function(numbers):
#     smallest = min(numbers)
#     largest = max(numbers)
#     my_tuple = (smallest, largest)  # ← tuple defined here
#     return my_tuple

# my_list = [3, 1, 7, 2, 9, 4]  # ← list defined here
# print(my_function(my_list))  # (1, 9)

    

# def my_function(numbers): 
#     return [num for num in numbers if num % 2 == 0]

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = my_function(my_list)
# print(result)  # [2, 4, 6, 8, 10]

# def my_function():
#     my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     numbers = int(input("what number would you like to pick from the list? "))
#     even = numbers % 2 == 0
#     odd = numbers % 2 != 0
#     if numbers not in my_list:
#         print("you didnt pick a number from the list")
#     elif even:
#         print("you picked an even number")
#     elif odd:
#         print("you picked an odd number")

# my_function()




# def my_function():
#     my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#     numbers = int(input("what grade did you get? "))

#     if numbers < 60 in my_list: 
#         print("error, try again")
#     elif numbers >= 60:
#         print("you passed the class")
#     elif numbers >= 90:
#         print("you got an A")
    
# my_function()


# def filter_above_threshold(numbers, threshold=10):
#     result = []
#     for num in numbers:
#         if num > threshold:
#             result.append(num)
#     return result

# my_list = [3, 15, 7, 22, 10, 11]
# print(filter_above_threshold(my_list))        # [15, 22, 11] (default threshold 10)
# print(filter_above_threshold(my_list, 20))    # [22] (threshold 20)



# def reverse_list(numbers, reverse=False):
#     if reverse:
#         return numbers[::-1]
#     return numbers

# my_list = [1, 2, 3, 4, 5]
# print(reverse_list(my_list))           # [1, 2, 3, 4, 5] (reverse=False)
# print(reverse_list(my_list, True))     # [5, 4, 3, 2, 1] (reverse=True)


# def get_evens(*args): 
#     my_list = []
#     for num in args: 
#         if num % 2 == 0:
#             my_list.append(num)
#     return my_list
# print(get_evens(1, 2, 3, 4, 5, 6))  # [2, 4, 6]


# def my_function(name, age):
#     print(f"Name: {name}, Age: {age}")

# my_function(name="Alice", age=25)  # keyword arguments
# my_function("Bob", 30)             # regular arguments

# def outer_function(numbers):
#     def inner_function():
#         return sum(numbers)
#     result = inner_function()
#     return result

# my_list = [1, 2, 3, 4, 5]
# print(outer_function(my_list))  # 13


# my_variable = 10  # defined outside

# def outer_function(numbers):
#     def inner_function():
#         return sum(numbers) + my_variable
#     result = inner_function()
#     return result

# my_list = [1, 2, 3, 4, 5]
# print(outer_function(my_list))  # 14


# def outer_function():
#     my_variable = 0
#     def inner_function():
#         nonlocal my_variable
#         my_variable = 10
#     inner_function()
#     return my_variable

# print(outer_function())  # 15


# def apply_function(my_list, func):
#     result = []
#     for item in my_list:
#         result.append(func(item))
#     return result

# def double(x):
#     return x * 2

# my_list = [1, 2, 3, 4, 5]
# print(apply_function(my_list, double))  # [2, 4, 6, 8, 10] #16

# def apply_to_number(func, number):
#     result = func(number)
#     return result

# def double(x):
#     return x * 2

# print(apply_to_number(double, 5))  # 17


# def filter_and_reverse(my_list, threshold, reverse=False):
#     result = []
#     for num in my_list:
#         if num > threshold:
#             result.append(num)
#     if reverse:
#         result = result[::-1]
#     return result

# my_list = [3, 15, 7, 22, 10, 11]
# print(filter_and_reverse(my_list, 10))        # [15, 22, 11]
# print(filter_and_reverse(my_list, 10, True))  # [11, 22, 15] #18

# def stats(*args):
#     total = sum(args)
#     biggest = max(args)
#     smallest = min(args)
#     my_tuple = (total, biggest, smallest)
#     return my_tuple

# print(stats(1, 2, 3, 4, 5))  # (15, 5, 1) #19


def split_even_odd(my_list):
    evens = []
    odds = []
    for num in my_list:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    my_tuple = (evens, odds)
    return my_tuple

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = split_even_odd(my_list)
print(f"Even numbers: {result[0]}")  # [2, 4, 6, 8]
print(f"Odd numbers: {result[1]}")   # [1, 3, 5, 7] #20

