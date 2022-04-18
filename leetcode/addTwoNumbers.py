# https://leetcode.com/problems/add-two-numbers/ 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nodeOne = l1
        nodeTwo = l2
        vaddi = 0
        result = ListNode(0)
        _res = result
        while nodeOne and nodeTwo:
            num = nodeOne.val + nodeTwo.val + vaddi
            vaddi = int(num / 10)
            _res.next = ListNode(num % 10)
            nodeOne = nodeOne.next
            nodeTwo = nodeTwo.next
            _res = _res.next
        while nodeOne:
            num = nodeOne.val + vaddi
            vaddi = vaddi = int(num/10)
            _res.next = ListNode(num % 10)
            nodeOne = nodeOne.next
            _res = _res.next
        while nodeTwo:
            num = nodeTwo.val + vaddi
            vaddi = int(num/10)
            _res.next = ListNode(num % 10)
            nodeTwo = nodeTwo.next
            _res = _res.next
        if vaddi > 0:
            _res.next = ListNode(vaddi)
        return result.next
        
