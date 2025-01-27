def welcome_user(name, age):
    return f"Welcome, {name}! You are {age} years old."

name = input("Enter your name: ")
age = input("Enter your age: ")

message = welcome_user(name, age)
print(message)
