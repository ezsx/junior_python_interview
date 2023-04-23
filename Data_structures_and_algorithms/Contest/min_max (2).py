n = int(input())
prices = list(map(int, input().split()))
# задавем направление тренда
cur_trend_list = ('min','max')
cf = 0
cur_trend = cur_trend_list[cf]
b = max(prices)
prices_min_max = []
min_max = []
days = []
d = prices[0]
for di, a in enumerate(prices):
    if a == b:
        continue
    # ищем мин и макс
    if (cur_trend == 'min') and (a < b) or (cur_trend == 'max') and (a > b):
        # тренд продолжаем
        d = a
        di_cur = di
    else:
        # тренд меняем
        cf += 1
        cur_trend = cur_trend_list[cf % 2]
        min_max.append(d)
        days.append(di_cur)
        if len(min_max) == 2:
            min_max.append(days)
            prices_min_max.append(min_max)
            min_max = []
            days = []
    b = a
if len(min_max) == 1 and min_max[0] != b and cf > 0:
    min_max.append(b)
    days.append(len(prices))
    min_max.append(days)
    prices_min_max.append(min_max)
print('Кол-во сделок', len(prices_min_max))
print(prices_min_max)
for d in prices_min_max:
    print(d[2][0])
    print(d[2][1])
#prices_min_max = sorted(prices_min_max, key=lambda x: x[1]-x[0],reverse=True)
#print(prices_min_max[:2])