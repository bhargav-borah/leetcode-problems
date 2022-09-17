prices = [7,6,4,3,1]


maxi = 0

for i in range(len(prices)-1):
    for j in range(i+1, len(prices)):
        profit = prices[j] - prices[i]
        maxi = max(maxi, profit)

print(maxi)