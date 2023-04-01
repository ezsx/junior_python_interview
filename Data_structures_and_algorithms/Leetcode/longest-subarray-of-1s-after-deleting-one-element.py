def longestSubarray(nums: list[int]) -> int:
    ans = sum = lo = 0
    for hi, num in enumerate(nums):
        sum += num
        if sum < hi - lo:
            sum -= nums[lo]
            lo += 1
        ans = max(ans, hi - lo)
    return ans
print(longestSubarray([0,1,1,1,0,1,1,0,1]))