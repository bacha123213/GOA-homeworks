#დავალება5
first_name = "Bacha"
correct_password = "Tkemaladze"
user_guess = input("Enter First Name: ")
user_guess = input("Enter last Name: ")
counter = 0

while user_guess != correct_password:
    user_guess = input("Enter Last Name: ")
    counter += 1