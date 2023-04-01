firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]

final_list = []
cuted = float("inf")
for gap1, gap2 in zip(firstList, secondList):
    if cuted == gap1[0]:
        final_list.append([cuted, gap1[0]])
    final_list.append([max(gap1[0], gap2[0]), min(gap1[1], gap2[1])])
    cuted = gap2[1]
print(final_list)
