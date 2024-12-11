um1 = int(input("Enter Ypur Number: "))
num2 = int(input("enter your second number: "))


numbers = []
if num1 > num2: 
    for i in range(num2, num1 + 1):
        if i % 2 == 0:
            print(f"{i} - even")
            numbers.append(i)
else:  
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            print(f"{i} - odd")
            numbers.append(i)
print("numb:", sum(numbers))