# https://leetcode.com/problems/summary-ranges/
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = len(nums)
        if l < 2:
            return list(map(lambda x: str(x), nums))
        start = nums[0]
        mid = nums[0]
        l = len(nums)
        result = [str(start)]
        resultIndex = 0
        index = 1
        while index < l:
            num = nums[index]
            if num == mid + 1:
                mid = num
            else:
                if mid != start:
                    result[resultIndex] += ('->' + str(mid))
                mid = num
                start = num
                resultIndex += 1
                result.append(str(num))
            index += 1
        if mid != start:
            result[resultIndex] += ('->' + str(mid))
        return result
