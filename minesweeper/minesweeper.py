def annotate(minefield: list[str]) -> list[str]:

    if not all(len(m) == len(minefield[0]) for m in minefield):
        raise ValueError("The board is invalid with current input.")
    
    if any(item not in ' *' for row in minefield for item in row):
        raise ValueError("The board is invalid with current input.")
    
    rows = len(minefield[0]) if minefield else 0
    cols = len(minefield)

    for idc, column in enumerate(minefield):
        for idr, row in enumerate(column):
            count = 0
            
            for posc in (-1, 0, 1):
                for posr in (-1, 0, 1):
                    if 0 <= idc + posc < cols and 0 <= idr + posr < rows:
                        if minefield[idc + posc][idr + posr] == '*':
                            count += 1
            col = list(minefield[idc])
            if minefield[idc][idr] != '*' and count:
                col[idr] = str(count)     
            minefield[idc] = ''.join(col) 

    return minefield

print(annotate(["   ", " * ", "   "]))


            # if minefield[idc][idr] != '*' and count:
            #     print('idc', idc, 'idr', idr, 'count', count)
            #     value += str(count)
            #     print('value', value)
            #     minefield[idc] = value
            #     print('minefield', minefield)