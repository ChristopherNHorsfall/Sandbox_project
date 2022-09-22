""""""

min_length = int(input("Minimum password length: "))
password = input("Enter password: ")
while len(password) < min_length:
    print("Password too short!")
    password = input("Enter password: ")
print("*" * len(password))
