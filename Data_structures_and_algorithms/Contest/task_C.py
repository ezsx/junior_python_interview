n = int(input())
prices = list(map(int, input().split()))
print(len(prices))
# задавем направление тренда
cur_trend_list = ('min','max')
cf = 0
cur_trend = cur_trend_list[cf]
b = max(prices)
prices_min_max = []
min_max = []
for a in prices:
    # ищем мин и макс
    if (cur_trend == 'min') and (a <= b) or (cur_trend == 'max') and (a > b):
        # тренд продолжаем
        d = a
    else:
        # тренд меняем
        cf += 1
        cur_trend = cur_trend_list[cf % 2]
        min_max.append(d)
        if len(min_max) == 2:
            prices_min_max.append(min_max)
            min_max = []
    b = a
if len(min_max) == 1:
    min_max.append(b)
    prices_min_max.append(min_max)
print(prices_min_max)