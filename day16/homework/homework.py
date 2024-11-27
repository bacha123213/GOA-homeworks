#while  ციკლი გამოიყენბა როდესაც ჩვენ არ ვიცით იტერაცია
#for ციკლი გამოიყენება როდესაც ჩვენ ვიცით თუ რამდენი იტერაცია გვაქ
for i in range(50):
    print("goa")
#დავალება2
counter = 1
while counter <= 10:
    print("counter")
    counter += 1
#დავალება3
counter = 2
while counter <= 20:
    print(counter)
    counter += 2 
#დავალება3
correct_password = "12345678"
user_23 = input("Enter password: ")
counter = 0

while user_23 != correct_password:
    user_23 = input("Enter password: ")
    counter += 1
#დავალება4
first_name = "Bacha"
correct_password = "Tkemaladze"
user_guess = input("Enter First Name: ")
user_guess = input("Enter last Name: ")
counter = 0

while user_guess != correct_password:
    user_guess = input("Enter Last Name: ")
    counter += 1