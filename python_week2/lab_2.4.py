# set([[1, 2], [3, 4]])

# set = {{1,2}, {3,4}} # This will raise an error because sets cannot contain mutable types like lists or other sets

# set_of_tuples = {(1, 2), (3, 4)}
# print(set_of_tuples)

# print((1,2) in set_of_tuples) # This will return True
# print((1,3) in set_of_tuples) # This will return False because (1,3) is not in the set of tuples    


developers = {"Alice", "Bob", "Charlie"}
admins = {"Alice", "David"}
print("Alice" in developers)
developers.union(admins) 
developers | admins 
developers.intersection(admins) 
developers & admins
developers.difference(admins)
developers - admins
union = developers.union(admins)
intersection = developers.intersection(admins)
difference = developers.difference(admins)
print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
