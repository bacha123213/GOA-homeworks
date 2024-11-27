correct_password = "paroliparoli"
while True:
    enter_password = input("Please enter your password: ")
    rint("Password correct. Access granted.")
    break  # Exit the loop when the correct password is entered
else:
     print("Incorrect password. Please try again.")