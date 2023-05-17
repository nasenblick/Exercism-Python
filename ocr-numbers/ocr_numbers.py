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

    columns = []
    rows = []
    col_count = max(len(c) for c in input_grid)

    i = 0    
    while i < col_count:
            columns = [s[i:i+3] for s in input_grid]
            rows.append(''.join(columns))
            i += 3
    return format(rows, resized)


def format(rows: list, resized: bool) -> str:
    result = []
    for number in rows:
        if number not in NUMBERS: 
            result += '?'
        for idx, item in enumerate(NUMBERS):
            if number == item: 
                result += str(idx)
                if idx % 3 == 0 and resized:
                    result += ','
    return ''.join(result).rstrip(',') if result else '?'


def resize(input_grid: list[str]) -> list[str]:
    resized_grid = []
    for idx, row in enumerate(input_grid):
        if 0 <= idx < 4:
            resized_grid.append(row)
        elif 4 <= idx < 8:
            resized_grid[idx-4] += row
        elif 8 <= idx < 12:
            resized_grid[idx-8] += row
        else:
            return -1
    return resized_grid
    
#print(convert([" _ ", "| |", "|_|", "   "]))


# print(convert(
#                 [
#                     "    _  _     _  _  _  _  _  _ ",
#                     "  | _| _||_||_ |_   ||_||_|| |",
#                     "  ||_  _|  | _||_|  ||_| _||_|",
#                     "                              ",
#                 ]))

print(convert([
                    "    _  _ ",
                    "  | _| _|",
                    "  ||_  _|",
                    "         ",
                    "    _  _ ",
                    "|_||_ |_ ",
                    "  | _||_|",
                    "         ",
                    " _  _  _ ",
                    "  ||_||_|",
                    "  ||_| _|",
                    "         ",
                ]))


