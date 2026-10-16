def max_profit(prices):

    lowest = prices[0]
    maxxx = 0

    for i in range(len(prices)):
        if lowest > prices[i]:
            lowest = prices[i]
        else:
            maxxx = max(maxxx, prices[i] - lowest)

    return maxxx 

prices = [[7,1,5,3,6,4],
          [7, 6, 4, 3, 1],
          [2, 4, 1],
          [5]]
for price in prices:
    print(max_profit(price))