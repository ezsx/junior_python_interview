# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: [TreeNode]) -> int:
        # Initialize the maximum path sum seen so far
        max_sum = float('-inf')

        # Define a recursive helper function that computes the maximum path sum
        def maxPathSumHelper(node):
            nonlocal max_sum

            # Base case: empty node
            if not node:
                return 0

            # Recursive case: compute the maximum path sum for the left and right subtrees
            left_sum = max(maxPathSumHelper(node.left), 0)
            right_sum = max(maxPathSumHelper(node.right), 0)

            # Compute the maximum path sum that goes through the current node
            node_sum = node.val + left_sum + right_sum

            # Update the maximum path sum seen so far
            max_sum = max(max_sum, node_sum)

            # Return the maximum path sum that goes through the current node
            return node.val + max(left_sum, right_sum)

        # Call the recursive helper function with the root node
        maxPathSumHelper(root)

        # Return the maximum path sum seen so far
        return max_sum
