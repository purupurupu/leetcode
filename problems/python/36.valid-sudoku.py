#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tmp_board = []
        for row in board:
            for i in range(1, 10):
                if row.count(str(i)) > 1:
                    return False
        # return True

        for i in range(9):
            for j in range(9):
                tmp_board.append(board[j][i])
            for k in range(1, 10):
                if tmp_board.count(str(k)) > 1:
                    return False
            tmp_board = []

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                for k in range(3):
                    for l in range(3):
                        tmp_board.append(board[i+k][j+l])
                for m in range(1, 10):
                    if tmp_board.count(str(m)) > 1:
                        return False
                tmp_board = []

        return True


board = [[".", ".", "4", ".", ".", ".", "6", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], ["5", ".", ".", ".", ".", ".", ".", "9", "."], [".", ".", ".", "5", "6", ".", ".", ".", "."], ["4", ".", "3", ".",
                                                                                                                                                                                                      ".", ".", ".", ".", "1"], [".", ".", ".", "7", ".", ".", ".", ".", "."], [".", ".", ".", "5", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."]]


tmp = Solution()
res = tmp.isValidSudoku(board)

print(res)

# @lc code=end
