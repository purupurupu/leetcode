#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
from typing import List

# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix[0])

        matrix.reverse()
        # print(matrix)

        for i in range(length):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                # matrix[i][j] = matrix[j][i]

        print(matrix)

# @lc code=end


n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

tmp = Solution()
res = tmp.rotate(n)
