my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = int(input("enter your number: "))

if index >= 0 and index < 10:  
    print("index element is:", my_list[index])

elif index >= -10 and index < 0: 
    print("index element is:", my_list[index])
else:
    print("is not list index.")