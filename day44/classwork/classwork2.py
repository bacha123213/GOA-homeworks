# 1)
def past(h, m, s):
    sum_of_seconds = 0
    
    # hour -> second
    sum_of_seconds += h * 3600
    
    # minute -> second
    sum_of_seconds += m * 60
    
    # second
    sum_of_seconds += s
    
    # result
    result = sum_of_seconds * 1000
    
    return result


# 2)

def find_needle(haystack):
    result = haystack.index("needle")
    return f"found the needle at position {result}"

# 3)

def invert(lst):
    new_list=[]
    for i in lst:
        new_list.append(i * -1)
    return new_list


# 4)

def smash(words):
    return " ".join(words)

# 5)

def grow(arr):
    product = 1

    for i in arr:
        product *= i

    return product
  

