# https://leetcode.com/submissions/detail/567730365/
# beats 94% in runtime
from copy import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)
        board_dict = {}
        for i in board:
            for j in i:
                board_dict[j] = board_dict.get(j, 0) + 1
        for i in word:
            if i in board_dict:
                if board_dict[i] > 0:
                    board_dict[i]-=1
                else:
                    return False
            else:
                return False
        
        m = len(board)
        n = len(board[0])
        def get_possible(i, j, val, i_lim, j_lim):
            l = [
                (i-1, j, val),
                (i, j-1, val),
                (i+1, j, val),
                (i, j+1, val)
            ]
            return list(filter(lambda _: i_lim > _[0] >= 0 and j_lim > _[1]>=0, l))    
        def find_path(i, j, selected, current_index):
            if (i, j) not in selected and board[i][j] == word[current_index]:
                if current_index == word_len-1:
                    return True
                selected.append((i, j))
                lst = get_possible(i, j, current_index + 1, m, n)
                for k in lst:
                    ii, jj, index = k
                    x = find_path(ii, jj, copy(selected), index)
                    if x:
                        return True
        for i in range(m):
            for j in range(n):
                x = find_path(i, j, [], 0)
                print(x)
                if x:
                    return True
        return False                
