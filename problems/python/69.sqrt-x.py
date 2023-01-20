#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        square = 0

        if x == 0:
            return 0

        # if x == 1:
        #     return 1

        while square < x:

            square = i * i

            if square == x:
                return i

            if square > x:
                return i-1

            i += 1
            # @lc code=end
