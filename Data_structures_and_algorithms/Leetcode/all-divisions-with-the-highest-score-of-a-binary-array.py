nums = [0, 0, 1, 0]
num_zeroes = nums.count(0)
num_ones = nums.count(1)
score_all = [num_ones]
zeroes_seen = 0
ones_seen = 0
for i in range(len(nums)):
    if nums[i] == 0:
        zeroes_seen += 1
    else:
        ones_seen += 1
    score_all.append(zeroes_seen + num_ones - ones_seen)
print(score_all)