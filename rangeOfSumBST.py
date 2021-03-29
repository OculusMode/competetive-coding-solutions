# https://leetcode.com/problems/range-sum-of-bst/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        if not root:
            return total
        if root.val >= low and root.val <= high:
            total += root.val
        if not root.val < low:
            total += self.rangeSumBST(root.left, low, high)
        if not root.val > high:
            total += self.rangeSumBST(root.right, low, high)
        return total
