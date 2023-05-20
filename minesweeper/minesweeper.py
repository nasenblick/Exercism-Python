def annotate(minefield: list[str]) -> list[str]:

    if not minefield:
        return minefield

    for row in minefield:
        if len(row) != len(minefield[0]) or any(c not in " *" for c in row):
            raise ValueError('The board is invalid with current input.')
    
    rows = len(minefield[0])
    cols = len(minefield)
    count = 0

    for idc, column in enumerate(minefield):
        for idr, row in enumerate(column):
            POSC = [idc - 1, idc - 1, idc - 1, idc + 1, idc + 1, idc, idc, idc + 1]
            POSR = [idr, idr - 1, idr + 1, idr, idr + 1, idr - 1, idr + 1, idr - 1]
            #if 0 < idc < cols - 1 and 0 < idr < rows - 1:
            print('idc',idc, 'idr', idr)
            for posc, posr in zip(POSC, POSR):
                if 0 <= posc < cols and 0 <= posr < rows:
                    if minefield [posc][posr] == '*':
                        count += 1
               
            if minefield[idc][idr] != '*' and count > 0:
                colTmp = list(minefield[idc])
                colTmp[idr] = str(count)
                minefield[idc] = "".join(colTmp)
            count = 0
    return minefield

print(annotate(["   ", " * ", "   "]))