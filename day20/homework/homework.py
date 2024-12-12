number = int(input("Enter a number: "))


if number <= 1:
    print(f"{number} is no prime number.")
else:
    
    is_prime = True
    
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False  
            break
    
    if is_prime:
        print("{number} is prime number.")
    else:
        print("{number} is no prime number.")