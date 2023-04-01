class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = {0: 1}  # initialize frequency of prefix sum 0 to 1
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
        return count

    def subarraySum1(self, nums: list[int], k: int) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                result += 1 if sum(nums[i:j + 1]) == k else 0
        return result
