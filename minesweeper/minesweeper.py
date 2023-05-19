def annotate(minefield):
    count = 0
    rows = len(minefield[0])
    cols = len(minefield)

    for idc, column in enumerate(minefield):
        for idr, row in enumerate(column):
            if idc < cols -1 and idr < rows -1:
                if minefield[idc + 1][idr] == '*':
                    count += 1
                if minefield[idc + 1][idr + 1] == '*':
                    count += 1
                if minefield[idc][idr + 1] == '*':
                    count += 1
                if minefield[idc][idr] != '*':
                    count = 8
                    colTmp = list(minefield[idc])
                    colTmp[0] = str(count)
                    minefield[idc] = "".join(colTmp)
            count = 0
    
    # #Ecke OL
    # if minefield[0][1] == '*':
    #     count += 1
    # if minefield[1][1] == '*':
    #     count += 1
    # if minefield[1][0] == '*':
    #     count += 1
    # if minefield[0][0] != '*':
    #     col0 = list(minefield[0])
    #     col0[0] = str(count)
    #     minefield[0] = "".join(col0)   
    # count = 0     

    # #Ecke OR
    # if minefield[cols - 2][0] == '*':
    #     count += 1
    # if minefield[cols - 2][1] == '*':
    #     count += 1
    # if minefield[cols - 1][1] == '*':
    #     count += 1
    # if minefield[cols - 1][0] != '*':
    #     colY = list(minefield[cols-1])
    #     colY[0] = str(count)
    #     minefield[cols-1] = ''.join(colY)
    # count = 0  

    # #Ecke UL
    # if minefield[0][rows - 2] == '*':
    #     count += 1
    # if minefield[1][rows - 2] == '*':
    #     count += 1
    # if minefield[1][rows - 1] == '*':
    #     count += 1
    # if minefield[0][rows - 1] != '*':
    #     row0 = list(minefield[0])
    #     row0[rows - 1] = str(count)
    #     minefield[0] = ''.join(row0)
    # count = 0


    # #Ecke UR
    # if minefield[cols - 2][rows - 1] == '*':
    #     count += 1
    # if minefield[cols - 2][rows - 2] == '*':
    #     count += 1
    # if minefield[cols - 1][rows - 2] == '*':
    #     count += 1
    # if minefield[cols -1][rows - 1] != '*':
    #     rowX = list(minefield[cols -1])
    #     rowX[cols - 1] = str(count)
    #     minefield[cols - 1] = ''.join(rowX)
    # count = 0
    
    return minefield

print(annotate(["   ", " * ", "   "]))