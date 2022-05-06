# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution:
    def removeDuplicates(self, s: str, k: int):
      top = [s[0], 0]
      stack = [top]
      for i in s:
        if stack and top[0] == i:
          temp = (top[1] + 1)%k
          if temp:
            top[1] = temp
          else:
            stack.pop()
            if stack:
                top = stack[-1]
        else:
          top = [i, 1]
          stack.append(top)
      _s = ''
      for i in stack:
        _s+=i[0]*i[1]
      return _s
