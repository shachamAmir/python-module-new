# Part 1 - Basic Function

def process_data_guarded(data):
    print(data)

# Exercise 2
process_data_guarded([])
process_data_guarded([1, 2, 3])

# Part 2 - Using len()

def process_data_guarded(data):
    print(f"processing {len(data)} items...")
    print("processed")

# Exercise 4
process_data_guarded([1, 2, 3])

# Exercise 5 - None causes TypeError
try:
    process_data_guarded(None)
except TypeError as e:
    print(f"TypeError")

# Part 3 - Guard Clause

def process_data_guarded(data):
    if not data:
        print("no data provided")
        return
    print(f"processing {len(data)} items...")
    print("processed")

# Exercise 7
process_data_guarded(None)
process_data_guarded([])

# Part 4 - Type check

def process_data_guarded(data):
    if not data:
        print("no data provided")
        return
    if not isinstance(data, list):
        print("invalid value for data. Please provide a list.")
        return
    print(f"processing {len(data)} items...")
    print("processed")

# Exercise 9
process_data_guarded("ABC")
process_data_guarded(10)

# Part 5 - Improved error message

def process_data_guarded(data):
    if not data:
        print("no data provided")
        return
    if not isinstance(data, list):
        print(f"invalid value type for data provided {type(data)} required list")
        return
    print(f"processing {len(data)} items...")
    print("processed")

# Exercise 11
process_data_guarded("ABC")

# Exercise 12
process_data_guarded(10)

# Part 6 - Without guards
def process_data_no_guard(data):
    print(f"processing {len(data)} items...")
    print("processed")

process_data_no_guard("ABC")  # works - string has len()
try:
    process_data_no_guard(10)  # crashes - int has no len()
except TypeError:
    print("TypeError")

# Part 7 - Full test
print("--- [] ---")
process_data_guarded([])

print("--- [1,2,3] ---")
process_data_guarded([1, 2, 3])

print("--- None ---")
process_data_guarded(None)

print("--- ABC ---")
process_data_guarded("ABC")

print("--- 10 ---")
process_data_guarded(10)



