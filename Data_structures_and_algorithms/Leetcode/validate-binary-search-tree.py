class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBSTUtil(root: TreeNode, min_val=float('-inf'), max_val=float('inf')) -> bool:
    if not root:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return (isBSTUtil(root.left, min_val, root.val) and
            isBSTUtil(root.right, root.val, max_val))

def isBST(root: TreeNode) -> bool:
    return isBSTUtil(root)


#
# class Solution:
#     def isValidBST(self, root: [TreeNode]) -> bool:

print(True+True+True)
