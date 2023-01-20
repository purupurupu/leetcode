#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend / divisor)

        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31

        return res
        # @lc code=end
