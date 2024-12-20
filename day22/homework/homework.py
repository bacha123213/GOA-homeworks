my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


num1 = int(input("enter your number (num1): "))
num2 = int(input("enter your secind number(num2): "))


if num1 > num2:
    new_list = my_list[num1:num2]
    print("list:", new_list)


elif num2 > num1:
   
    new_list = my_list[num2:num1]
    print("list:", new_list)

else:
    print("empty liste:", [])