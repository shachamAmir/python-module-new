# Working with dictionaries only
def greet():
    print("Hello world!")

car1 = {
    "brand": "Toyota",
    "model": "yaris",
    "year": 2015,
    "tank": 1.6,
    "is_active": True,
    "say_hello": greet
}

car1["say_hello"]()

car2 = {
    "brand": "Toyota",
    "model": "yaris",
}