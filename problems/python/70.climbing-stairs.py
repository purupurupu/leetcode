#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        array = []
        # conbination?
        if n == 1 or n == 2:
            return n

        for i in range(n):

            if i == 0:
                array.append(1)
            elif i == 1:
                array.append(2)
            else:
                array.append(array[i-2] + array[i-1])

        return array[n-1]
        # @lc code=end
