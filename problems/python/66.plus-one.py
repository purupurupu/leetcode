#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s: str = ""
        ss: str = ""
        res = []
        for v in digits:
            s = s + str(v)
        # print(s)

        i = int(s) + 1
        ss = str(i)

        for v in ss:
            # print(v)
            res.append(v)

        # print(res)
        return res
        # @lc code=end
