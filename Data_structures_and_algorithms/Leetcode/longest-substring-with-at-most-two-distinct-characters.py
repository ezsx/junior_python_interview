class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n

        left = 0
        right = 0
        freq = {}
        max_len = 2

        while right < n:
            if len(freq) < 3:
                freq[s[right]] = right
                right += 1

            if len(freq) == 3:
                del_idx = min(freq.values())
                del freq[s[del_idx]]
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len
