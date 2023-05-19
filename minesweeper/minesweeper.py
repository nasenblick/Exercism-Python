def annotate(minefield):

    rows = any(len(m) for m in minefield)
    cols = len(minefield)
    count = 0

    if not rows:
        return minefield
    
    if not all(len(m) == len(minefield[0]) for m in minefield):
        raise ValueError("The board is invalid with current input.")

    if any(item != ' ' and item != '*' for row in minefield for item in row):
        raise ValueError("The board is invalid with current input.")

    for idc, column in enumerate(minefield):
        for idr, row in enumerate(column):
            try:
                if idc > 0 and minefield[idc - 1][idr] == '*':
                    count += 1
            except IndexError:
                pass

            try:
                if idc > 0 and idr > 0 and minefield[idc - 1][idr - 1] == '*':
                    count += 1
            except IndexError:
                pass

            try:
                if idc > 0 and minefield[idc - 1][idr + 1] == '*':
                    count += 1
            except IndexError:
                pass
            
            try:
                if minefield[idc + 1][idr] == '*':
                    count += 1
            except IndexError:
                pass
                
            try:
                if minefield[idc + 1][idr + 1] == '*':
                    count += 1
            except IndexError: 
                pass
        
            try:
                if idr > 0 and minefield[idc][idr - 1] == '*':
                    count += 1
            except IndexError:
                pass
                
            try:
                if minefield[idc][idr + 1] == '*':
                    count += 1
            except IndexError: 
                pass
                
            try:
                if idr > 0 and minefield[idc + 1][idr - 1] == '*':
                    count += 1
            except IndexError: 
                pass
                
            if minefield[idc][idr] != '*' and count > 0:
                colTmp = list(minefield[idc])
                colTmp[idr] = str(count)
                minefield[idc] = "".join(colTmp)
            count = 0
    return minefield

print(annotate([" ", "*  ", "  "]))