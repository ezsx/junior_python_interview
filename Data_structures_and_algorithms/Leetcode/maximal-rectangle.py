class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix[0])     # len row
        height = [0] * (m + 1) # current row of histogram
        ans = 0

        for row in matrix:
            for i in range(m): # upping current row by 1
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1] # init stack
            for i in range(m + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)

        return ans