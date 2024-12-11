def chec_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

num = float(input("Enter a number: "))


result = chec_sign(num)


print(f"The number {num} is {result}.")