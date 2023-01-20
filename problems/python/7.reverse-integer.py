#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sx = str(x)
        flag = False

        if sx[0] == "-":
            sx = sx[1:]
            flag = True

        rsx = sx[::-1]
        if flag == True:
            rsx = "-" + rsx

        if int(rsx) > (2**31) - 1:
            return 0

        if int(rsx) < -(2**31):
            return 0

        return int(rsx)
        # @lc code=end
