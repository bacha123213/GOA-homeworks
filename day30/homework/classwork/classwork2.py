def manual_find(main_string, str_to_find):
    index = main_string.find(str_to_find)
    if index == -1:
        print(-1)
    else:
        print(index)
