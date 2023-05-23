CELLS = [(posc, posr) for posc in (-1, 0, 1) for posr in (-1, 0, 1)]


def annotate(minefield: list[str]) -> list[str]:

    if not all(len(m) == len(minefield[0]) for m in minefield):
        raise ValueError("The board is invalid with current input.")
    
    if any(item not in ' *' for row in minefield for item in row):
        raise ValueError("The board is invalid with current input.")
    
    rows = len(minefield[0]) if minefield else 0
    cols = len(minefield)
    

    for idc, column in enumerate(minefield):
        col = []
        for idr in range(len(column)):
            count = sum(1 for posc, posr in CELLS if 0 <= idc + posc < cols and 0 <= idr + posr < rows and minefield[idc + posc][idr + posr] == '*')

            col.append(-1) if minefield[idc][idr] == '*' else col.append(count)

        col_tmp = [str(cell) for cell in col]
        col_str = ''.join(col_tmp)
        col_str = col_str.replace('0', ' ').replace('-1', '*')
        minefield[idc] = col_str
    return minefield



print(annotate(["***", "   ", "   "]))


            # if minefield[idc][idr] != '*' and count:
            #     print('idc', idc, 'idr', idr, 'count', count)
            #     value += str(count)
            #     print('value', value)
            #     minefield[idc] = value
            #     print('minefield', minefield)