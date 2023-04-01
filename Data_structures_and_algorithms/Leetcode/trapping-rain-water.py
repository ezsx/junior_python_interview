def pars_lvls(cur_lvl, height):
    height1 = height.copy()
    for i in range(len(height1)):
        height1[i] -= cur_lvl
        if height1[i] < 0:
            height1[i] = 0
        if height1[i] > 0:
            height1[i] = 1
    return height1


def find_water_in_gap(arr):
    sm = abs(sum(arr) - len(arr))
    if arr[-1] == 0:
        for i in arr[::-1]:
            if i == 0:
                sm -= 1
            else:
                break
    if arr[0] == 0:
        for i in arr:
            if i == 0:
                sm -= 1
            else:
                break
    return sm

height = [1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
levels = [i for i in range(max(height))]
print(levels)

total_water = 0
for i in levels:
    total_water += find_water_in_gap(pars_lvls(i, height))
print(total_water)
