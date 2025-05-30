#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        
        prev_row = self.getRow(rowIndex - 1)
        return [1] + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)] + [1]

        
# @lc code=end

print(Solution().getRow(3))
print(Solution().getRow(0))
print(Solution().getRow(1))
