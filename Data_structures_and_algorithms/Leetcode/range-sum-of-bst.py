# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0

            if node.val < low:
                # Traverse right subtree only, as left subtree will have even smaller values
                return dfs(node.right)
            elif node.val > high:
                # Traverse left subtree only, as right subtree will have even greater values
                return dfs(node.left)
            else:
                # Node value is within the range, add its value and traverse both subtrees
                return node.val + dfs(node.left) + dfs(node.right)

        return dfs(root)