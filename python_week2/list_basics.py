number_int = 6 # integer
number_float = 6.0 # float
string = "babe" # string
boolers = False # boolean (0)
boolers2 = True # boolean (1)

# List
book1 = "harry potter and the philosopher's stone"
book2 = "harry potter and the chamber of secrets"
book3 = "harry potter and the prisoner of azkaban"
book4 = "harry potter and the goblet of fire"
book5 = "harry potter and the order of the phoenix"
book6 = "harry potter and the half-blood prince"
book7 = "harry potter and the deathly hallows"

harry_potter_books = [
    "harry potter and the philosopher's stone",
    "harry potter and the chamber of secrets",
    "harry potter and the prisoner of azkaban",
    "harry potter and the goblet of fire",
    "harry potter and the order of the phoenix",
    "harry potter and the half-blood prince",
    "harry potter and the deathly hallows"
]
print(harry_potter_books[3]) 

multi_data_list = [ 
    "babe", 
    1.2, 
    54,
    True,
    ["Amir Shacham"]
]
print(type(multi_data_list[0])) # string
print(type(multi_data_list[1])) # float
print(type(multi_data_list[2])) # int

# List
my_list = ["Bob", "Rolf", "Anne"]
print(my_list[1])
print(my_list)

# Tuple
my_tuple = ("Bob", "Rolf", "Anne")
print(my_tuple[1])
print(my_tuple)

# Set
my_set = {"Bob", "Rolf", "Anne"}
print(my_set)


name = "Jordan"
# name[0] = "5" # ! Expect to get Jordan but wont work cause string are imutable
my_list = ["Bob", "Rolf", "Anne"]
print(my_list)
my_list[0] = "Smith"
print(my_list)

my_servers = [
    "us-east-1",
    "us-west-1",
    "eu-west-1"
    "il-west-1"
]
my_tuple = ("Bob", "Rolf", "Anne")
print(my_tuple)
# my_tuple[0] = "Smith"  #! This will raise an error because tuples are immutable

# Adding to a list
my_list.append("John")
print(my_list)

# my_tuple.append("John")  #! This will raise an error because tuples are immutable

# Removing from a list
my_list.remove("Rolf")
print(my_list)

# Trying to mutate a list inside a tuple
my_tuple = ("Bob", "Rolf", "Anne", ["John", "Smith"])
print(my_tuple)
my_tuple[3].append("Doe")
print(my_tuple)

