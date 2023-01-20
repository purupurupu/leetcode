#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:

    strCount = 0
    index = 0

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        for i, val in enumerate(strs):
            if i == 0:
                strCount = len(val)
                index = i
            # strCount = len(val)
            if len(val) < strCount:
                strCount = len(val)
                index = i
            # print(strCount)
            # print(index)

        targetString = strs[index]
        eraseFlag = False
        # stringCount = 200
        firstFlag = False
        tmpRes = ""
        res = ""

        for i, val in enumerate(strs):
            endFlag = False

            if (i == index):
                continue

            for j in range(len(targetString)):
                if targetString[j] == val[j]:
                    res = res + val[j]

                else:
                    endFlag = True

                if endFlag == True:
                    if res == "":
                        eraseFlag = True
                    break

            if firstFlag == False:
                tmpRes = res
                firstFlag = True
            elif len(tmpRes) > len(res):
                tmpRes = res

            res = ""

        if eraseFlag == True:
            return ""
        return tmpRes
        # @lc code=end
