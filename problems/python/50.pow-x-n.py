#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:

        fixedNum = x
        negFlag = False  # init

        if n == 0 or x == 1:
            return 1

        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1

        if n < 0:
            negFlag = True
            n = abs(n)

        for i in range(n-1):
            x = x * fixedNum

            if abs(x * 100000) < 1:
                return 0

            if negFlag == True and abs(1/x * 100000) < 1:
                return 0

        if negFlag == True:
            return 1/x
        else:
            return x
# @lc code=end
