st = int(input("Enter the starting number: "))
en = int(input("Enter the ending number: "))
sum = 0

for number in range(st, en + 1):
    sum += number

print("The sum of numbers between {st} and {en} is: {sum}")