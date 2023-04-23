nums = [23, 2, 4, 6, 7]
k = 6

chunk = 2
i = 0
while chunk != len(nums):
    if sum(nums[i:i + chunk]) % k == 0 and len(nums[i:i + chunk]) >= 2:
        print(True, nums[i:i + chunk])
        break
    if i + chunk == len(nums):
        i = 0
        chunk += 1
    i += 1
print(False)
