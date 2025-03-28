def get_count(string):
    vowels = "aeiou"
    return sum(1 for char in string if char in vowels)
