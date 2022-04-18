# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff not in hashMap:
                hashMap[val] = i
            else:
                return [hashMap[diff], i]
        return []
