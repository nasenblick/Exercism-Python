CELLS = []
for posc in (-1, 0, 1):
    for posr in (-1, 0, 1):
        CELLS.append((posc, posr))

def annotate(minefield: list[str]) -> list[str]:

    if not all(len(m) == len(minefield[0]) for m in minefield):
        raise ValueError("The board is invalid with current input.")
    
    if any(item not in ' *' for row in minefield for item in row):
        raise ValueError("The board is invalid with current input.")
    
    rows = len(minefield[0]) if minefield else 0
    cols = len(minefield)

    for idc, column in enumerate(minefield):
        for idr in range(len(column)):
            count = 0
            tmp = []
            
            #count += 1 for posc, posr in CELLS if 0 <= idc + posc < cols and 0 <= idr + posr < rows and minefield[idc + posc][idr + posr] == '*'
            for posc, posr in CELLS:
                if 0 <= idc + posc < cols and 0 <= idr + posr < rows and minefield[idc + posc][idr + posr] == '*':
                    count += 1
            
            
            
            if minefield[idc][idr] != '*' and count:
                 tmp += str(count)
         
                
            col = list(minefield[idc])
            col[idr] = str(count)     
            minefield[idc] = ''.join(col) 
            


            



        #     if minefield[idc][idr] != '*' and count:
        #         print('count', count)
        #         print('idc', idc)
        #         print('tmp', tmp)
        #         tmp.append(count)

        # minefield[idc] = tmp  

    return minefield


def format(minefield):
            pass

print(annotate(["   ", " * ", "   "]))


            # if minefield[idc][idr] != '*' and count:
            #     print('idc', idc, 'idr', idr, 'count', count)
            #     value += str(count)
            #     print('value', value)
            #     minefield[idc] = value
            #     print('minefield', minefield)