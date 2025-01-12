def manual_index(main_str, search_str):
   
    index = main_str(search_str)
    
    if index != -1:
        print(f"'{search_str} {index}")
    else:
        print(f"'{search_str}'")