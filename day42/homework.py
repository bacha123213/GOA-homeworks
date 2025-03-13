def manual_list(start, end, step, user_num):
    result = [num + user_num for num in range(start, end, step)]
    return result
print(manual_list(2, 15, 2, 4))

