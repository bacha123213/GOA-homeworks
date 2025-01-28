def manual_swapcase(input_string):
    swapped_string = ""   
    for char in input_string:    
        if char.isupper():
            swapped_string += char.lower()
            swapped_string += char.upper()
        else:
            swapped_string += char
    
    return swapped_string
print(manual_swapcase("bacho!"))
print(manual_swapcase("123"))
