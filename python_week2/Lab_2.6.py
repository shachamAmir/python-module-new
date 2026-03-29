friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local = friends.difference(abroad)
print(local)

print(abroad.difference(friends) )

local = {"Rolf"}
abroad = {"Bob", "Anne"}
friends = local.union(abroad)
print(friends)


local | abroad
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
print(art.intersection(science))

art & science 
print("Bob" in art)
print("Anne" in art)

