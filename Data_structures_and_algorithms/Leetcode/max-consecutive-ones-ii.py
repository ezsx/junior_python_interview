class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        prev_length = curr_length = max_length = 0
        flipped_zero = False

        for num in nums:
            if num == 1:
                curr_length += 1
            else:
                if flipped_zero:
                    max_length = max(max_length, prev_length + curr_length)
                    prev_length = curr_length
                    curr_length = 0
                else:
                    flipped_zero = True
                    prev_length = curr_length + 1
                    curr_length = 0

        # Check if the last sequence of ones needs to be included in the maximum length
        if flipped_zero:
            max_length = max(max_length, prev_length + curr_length)
        else:
            max_length = curr_length

        return max_length
