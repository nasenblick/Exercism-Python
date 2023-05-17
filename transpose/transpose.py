def transpose(lines: list[str]) -> str:
    max_len = 0
    for line in lines:
        max_len = max(max_len, len(line))

    result = ''
    for i in range(max_len):
        column = ''
        for j in range(len(lines)):
            if i < len(lines[j]):
                column += lines[j][i]
            else:
                column += ' '
        result += column + '\n'
    
    return ''.join(result).rstrip('\n')

print(transpose(["A1"]))
print(transpose(["A", "1"]))
print(transpose(["ABC", "123"]))