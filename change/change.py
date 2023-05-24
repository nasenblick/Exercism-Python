def find_fewest_coins(coins, target):
    change = []
    while target:
        for coin in coins[::-1]:
            if target >= coin:
                change.append(coin)
                target -= coin
    return change

print(find_fewest_coins([1, 4, 15, 20, 50], 23))