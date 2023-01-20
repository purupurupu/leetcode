#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        count = 0
        spaceFlag = False
        countInFalse = 0

        for v in s:

            if v == " ":
                spaceFlag = True
                if count > res:
                    res = count
                    count = 0
                count = 0

            elif v.isalnum() == True and spaceFlag == True:
                count += 1
                res = count

            elif spaceFlag == False:
                countInFalse += 1

        if spaceFlag == False and res == 0:
            return countInFalse

        elif spaceFlag == True and res == 0:
            return countInFalse

        if res == 0:
            return count

        return res
        # @lc code=end
