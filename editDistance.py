# https://leetcode.com/problems/edit-distance/
class Solution:
    def minDistance(self, a: str, b: str) -> int:
         # initialising lengths
        lenA = len(a) # for vertical
        lenB = len(b) # for horizontal
        # creating table
        table = [[0 for i in range(lenA + 1)] for j in range(lenB + 1)]
        # initalizing table(first rows and columns as i)
        for i in range(1, lenB + 1):
            table[i][0] = i
        for i in range(1, lenA + 1):
            table[0][i] = i
        for i in range(1, lenB + 1):
            for j in range(1, lenA + 1):
                d = 0 if b[i - 1] == a[j - 1] else 1
                up = table[i - 1][j] + 1 # for insertion
                left = table[i][j - 1] + 1 # for deletion
                upLeft = table[i-1][j-1] # for altering (so if altered, d will be 1 so we increase 1)
                table[i][j] = min(up, left, upLeft + d)

        # printTable(['', *list(b)], ['' ,*list(a)], table)

        return table[lenB][lenA]
        
