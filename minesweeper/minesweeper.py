CELLS = [(posc, posr) for posc in (-1, 0, 1) for posr in (-1, 0, 1)]


def annotate(minefield: list[str]) -> list[str]:

    if not all(len(m) == len(minefield[0]) for m in minefield):
        raise ValueError("The board is invalid with current input.")
    
    if any(item not in ' *' for row in minefield for item in row):
        raise ValueError("The board is invalid with current input.")
    
    rows = len(minefield[0]) if minefield else 0
    cols = len(minefield)
    result = []

    for idc, column in enumerate(minefield):
        col = []
        for idr in range(len(column)):
            count = sum(
                0 <= idc + posc < cols and 0 <= idr + posr < rows 
                and minefield[idc + posc][idr + posr] == '*' 
                for posc, posr in CELLS)
            
            if minefield[idc][idr] == '*':
                col.append('*')
            elif count == 0:
                col.append(' ')
            else: 
                col.append(str(count))

            #col += '*' if minefield[idc][idr] == '*' else ' ' if count == 0 else str(count)
        result.append(''.join(col))
    return result



print(annotate(["   ", "   ", "   "]))


            # if minefield[idc][idr] != '*' and count:
            #     print('idc', idc, 'idr', idr, 'count', count)
            #     value += str(count)
            #     print('value', value)
            #     minefield[idc] = value
            #     print('minefield', minefield)