# https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        l = [root]
        v = []
        while l:
            z = l.pop()
            v.append(z.val)
            if z.children:
                l.extend(reversed(z.children))
        return v
