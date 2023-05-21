def annotate(minefield: list[str]) -> list[str]:

    for row in minefield:
        if len(row) != len(minefield[0]) or any(c not in " *" for c in row):
            raise ValueError('The board is invalid with current input.')
    
    rows = len(minefield[0]) if minefield else 0
    cols = len(minefield)

    for idc, column in enumerate(minefield):
        for idr, row in enumerate(column):
            count = 0
            for posc in (-1, 0, 1):
                for posr in (-1, 0, 1):
                    if 0 <= idc + posc < cols and 0 <= idr + posr < rows:
                        print('idc', idc, 'posc', posc, 'idr', idr, 'posr', posr)
                        if minefield[idc + posc][idr + posr] == '*':
                            count += 1

                    if minefield[idc][idr] != '*' and count > 0:
                        col_tmp = list(minefield[idc])
                        col_tmp[idr] = str(count)
                        minefield[idc] = "".join(col_tmp)
    return minefield

print(annotate(["   ", " * ", "   "]))