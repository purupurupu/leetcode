#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        tmpArr = []

        for i, val in enumerate(s):

            if val == ")" and "(" in tmpArr and tmpArr[-1] == "(":
                # tmpArr.remove("(")
                tmpArr.pop(-1)
                continue

            if val == "}" and "{" in tmpArr and tmpArr[-1] == "{":
                # tmpArr.remove("{")
                tmpArr.pop(-1)
                continue

            if val == "]" and "[" in tmpArr and tmpArr[-1] == "[":
                # tmpArr.remove("[")
                tmpArr.pop(-1)
                continue

            tmpArr.append(val)

        if len(tmpArr) > 0:

            return False

        return True
        # @lc code=end
