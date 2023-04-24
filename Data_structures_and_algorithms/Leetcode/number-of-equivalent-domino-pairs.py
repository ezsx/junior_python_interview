
class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        count = 0
        seen = {}
        for domino in dominoes:
            key = tuple(sorted(domino))
            if key in seen:
                count += seen[key]
                seen[key] += 1
            else:
                seen[key] = 1
        return count