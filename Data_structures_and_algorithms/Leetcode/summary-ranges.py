nums = [0,1,2,4,5,7]+[-1]

ranges = []
cur_start = nums[0]
for i in range(1, len(nums)):
    if nums[i] - nums[i - 1] != 1:
        if cur_start == nums[i-1]:
            ranges.append(str(cur_start))
        else:
            ranges.append(str(cur_start)+"->"+ str(nums[i - 1]))
        cur_start=nums[i]


print(ranges)
