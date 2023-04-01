nums = [2, 7, 11, 15]
target = 9
res = []

for i in range(len(nums)):
    for j in range(i, len(nums)):
        if i == j:
            continue
        if nums[i] + nums[j] == target:
            res += [i] + [j]
print(res)

checked = {}
i = 0
while target - nums[i] not in checked:
    checked[nums[i]] = i
    i += 1
print(checked)
aa=[checked[target - nums[i]], i]
print(aa)
