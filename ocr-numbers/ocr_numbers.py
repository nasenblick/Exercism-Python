NUMBERS = [
    ' _ | ||_|   ',
    '     |  |   ',
    ' _  _||_    ',
    ' _  _| _|   ',
    '   |_|  |   ',
    ' _ |_  _|   ',
    ' _ |_ |_|   ',
    ' _   |  |   ',
    ' _ |_||_|   ',
    ' _ |_| _|   '
    ]

def convert(input_grid: list[str]) -> str: 
    if len(input_grid) % 4 != 0: 
        raise ValueError("Number of input lines is not a multiple of four") 
    if any(len(s) % 3 != 0 for s in input_grid): 
        raise ValueError("Number of input columns is not a multiple of three")
    
    resized = False
    
    if len(input_grid) > 4:
        resized = True
        input_grid = resize(input_grid)

    rows = [''.join([input_grid[i][j:j+3] for i in range(len(input_grid))]) for j in range(0, len(input_grid[0]), 3)]
    return format(rows, resized)

def format(rows: list, resized: bool) -> str: 
    result = [] 
    for number in rows: 
        if number not in NUMBERS: 
            result.append('?') 
        else: result.append(str(NUMBERS.index(number))) 
            
        if NUMBERS.index(number) % 3 == 0 and resized: 
            result.append(',') 
    return ''.join(result).rstrip(',') if result else '?'

def resize(input_grid: list[str]) -> list[str]: 
    resized_grid = [] 
    for idx, row in enumerate(input_grid): 
        if 0 <= idx < 4: 
            resized_grid.append(row) 
        else: 
            resized_grid[idx % 4] += row 
    return resized_grid

#print(convert([" _ ", "| |", "|_|", "   "]))


print(convert(
                [
                    "    _  _     _  _  _  _  _  _ ",
                    "  | _| _||_||_ |_   ||_||_|| |",
                    "  ||_  _|  | _||_|  ||_| _||_|",
                    "                              ",
                ]))

# print(convert([
#                     "    _  _ ",
#                     "  | _| _|",
#                     "  ||_  _|",
#                     "         ",
#                     "    _  _ ",
#                     "|_||_ |_ ",
#                     "  | _||_|",
#                     "         ",
#                     " _  _  _ ",
#                     "  ||_||_|",
#                     "  ||_| _|",
#                     "         ",
#                 ]))


