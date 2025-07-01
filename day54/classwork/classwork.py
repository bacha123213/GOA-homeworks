
num1 = float(input("Enter numerator: "))
num2 = float(input("Enter denominator: "))

try:
    print(num1/num2)
except ValueError:
    raise ValueError("Denominator cannot be equel to zero")
except:
    print("invalid input")
finally:
    print("Operation is completed")




#Write a function apply_to_list(func, values) that takes a function func and a list values, and returns a new list where func is applied to each element.Then: Define a function square(x) that returns the square of a number.

def square(x):
    return x**2

def apply_to_list(func, values):
    new_list = []

    for i in values:
        new_list.append(func(i))
    
        return new_list

print(apply_to_list(square, list(range(10))))