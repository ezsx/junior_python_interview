nums = [3, 6, 1, 0]


def sol(nums):
    nums_a = nums[:]
    max1 = nums_a.index(max(nums_a))
    temp_max_1 = nums_a[max1]
    del nums_a[max1]
    max2 = max(nums_a)
    if temp_max_1 // 2 >= max2:
        return max1
    else:
        return -1


print(sol(nums))
