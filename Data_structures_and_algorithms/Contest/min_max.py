n = int(input())
prices = list(map(int, input().split()))
cur_trend_list = ('min', 'max')
cf = 0
cur_trend = cur_trend_list[cf]
b = max(prices)
prices_min_max = []
min_max = []
d = prices[0]
index = 0

for i, a in enumerate(prices):
    if a == b:
        continue

    if (cur_trend == 'min') and (a < b) or (cur_trend == 'max') and (a > b):
        d = a
    else:
        cf += 1
        cur_trend = cur_trend_list[cf % 2]
        min_max.append(index + 1)  # Add 1 to the index
        if len(min_max) == 2:
            prices_min_max.append(min_max)
            min_max = []
    b = a
    index = i

if len(min_max) == 1 and min_max[0] != index and cf > 0:
    min_max.append(index + 1)  # Add 1 to the index
    prices_min_max.append(min_max)

prices_min_max = sorted(prices_min_max, key=lambda x: prices[x[1] - 1] - prices[x[0] - 1], reverse=True)
print(len(prices_min_max[:2]))

for pair in prices_min_max:
    print(pair[0], pair[1])
