def no_duplicates(user_list):
    return list(set(user_list))


print(no_duplicates([1, 2, 3, 4, 5, 5, 6])) 
print(no_duplicates(['e', 'n', 'a', 'o']))  
print(no_duplicates([1, 2, 2, 3, 3, 3, 4]))
