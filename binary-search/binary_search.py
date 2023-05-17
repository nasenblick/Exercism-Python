def find(search_list, value):
    right = len(search_list)
    left = 0
    
    while right > left:
        middle = (left + right) // 2 
        if search_list[middle] == value:
            return middle
        elif search_list[middle] > value:
            return find(search_list[middle], value)
        elif search_list[middle] < value:
            return find(search_list[middle + 1], value)
 
    raise ValueError("value not in array")

print(find([1, 3, 4, 6, 8, 9, 11], 8))
    