nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]

print((set(nums).symmetric_difference(set([i for i in range(len(nums)+1)]))).pop())
