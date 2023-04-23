# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: [TreeNode]) -> list[list[int]]:
        if root is None:
            return []

        res = []
        queue = [root]
        turn = False

        while queue:
            level = []
            next_queue = []

            for node in queue:
                level.append(node.val)

                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)

            if turn:
                level.reverse()
            res.append(level)
            turn = not turn
            queue = next_queue

        return res