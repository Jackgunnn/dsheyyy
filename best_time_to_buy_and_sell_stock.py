def max_profit(prices):

    maxi = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            diff = prices[j] - prices[i]
            # print(i, diff)
            if diff > maxi:
                maxi = diff

    return maxi


prices = [[7,1,5,3,6,4],
          [7, 6, 4, 3, 1],
          [2, 4, 1],
          [5]]
for price in prices:
    print(max_profit(price))