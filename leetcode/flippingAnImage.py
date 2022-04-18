# https://leetcode.com/problems/flipping-an-image/
def invert(num: int) -> int:
        return 0 if num == 1 else 1
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in A:
            l = len(A)
            for j in range(ceil(l/2)):
                i[j], i[l - 1 -j] = invert(i[l - 1 - j]), invert(i[j])
        return A
