import os
print("I am running from:", os.getcwd())
print("My file is at:", __file__)

with open("test_working.txt", "w") as f:
    f.write("Hello Kelly! It works!")

print("Created test_working.txt!")