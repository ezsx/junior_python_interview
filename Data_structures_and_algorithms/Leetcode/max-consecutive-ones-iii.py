nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3

i = 0
for j in range(len(nums)):
    k -= 1 - nums[j]
    if k < 0:
        k += 1 - nums[i]
        i += 1
print(j - i + 1)
