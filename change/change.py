def find_fewest_coins(coins: list[str], target: int) -> list[str]:
    result = []

    for i in range(len(coins)):
        if give_change(coins, target):
            result.append(give_change(coins, target))
        coins.pop()
        #print(result)
    return min(result, key=len)


def give_change(coins: list[str], target: int) -> list[str]:
    change = []
    while target > 0:
        for coin in [5, 2]:#coins[::-1]:
            print(target)
            print(coin)
            
            if target >= coin:
                change.append(coin)
                print(change)
                print('---')
                target -= coin
                break
            if target < min(coins):
                #print(min(coins))
                return 0
    return change

#print(give_change([1, 4, 15], 23))
#print(give_change([1, 4, 15, 20, 50], 23))
#print(find_fewest_coins([1, 4, 15, 20, 50], 23))
print(give_change([2, 5, 10, 20, 50], 21))
#print(find_fewest_coins([2, 5, 10, 20, 50], 21))


