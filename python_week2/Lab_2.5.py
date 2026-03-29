packages = ["python3", "pip", "requests", "boto3", "pip", "paramiko"]
print(("requests") in packages)
print(("ansible") in packages)
print(f"Is 'requests' required? {'requests' in packages}")
print(f"Is 'ansible' required? {'ansible' in packages}")

# Exercise 7 - convert to set to remove duplicates
required_packages = set(packages)

# Exercise 8 - remove "pip" safely
required_packages.discard("pip")

# Exercise 9 - print after changes
print(required_packages)

# Exercise 10 - create installed_packages set
installed_packages = {"docker", "python3", "pip"}

missing_packages = required_packages - installed_packages
print(f"Missing packages: {missing_packages}")
extra_packages = installed_packages - required_packages
print(f"Extra packages: {extra_packages}")
common_packages = required_packages & installed_packages
print(f"Common packages: {common_packages}")
