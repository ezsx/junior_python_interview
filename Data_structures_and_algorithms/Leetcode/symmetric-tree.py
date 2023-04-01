class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True

    def checkSymmetry(left_node: TreeNode, right_node: TreeNode) -> bool:
        # Both nodes are None, symmetric
        if not left_node and not right_node:
            return True

        # One of the nodes is None, not symmetric
        if not left_node or not right_node:
            return False

        # Check if the current nodes' values are equal, and
        # check symmetry for the left and right subtrees
        return (left_node.val == right_node.val) and \
               checkSymmetry(left_node.left, right_node.right) and \
               checkSymmetry(left_node.right, right_node.left)

    return checkSymmetry(root.left, root.right)

# Test case
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))  # Output: True
