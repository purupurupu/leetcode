#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        tmp = []
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # print(tmp)
        for v in digits:
            tmp.append(map[v])
        # print(tmp)

        length = len(digits)
        if length == 0:
            return res

        if length == 1:
            for i in tmp[0]:
                res.append(i)

        if length == 2:
            for i in tmp[0]:
                for j in tmp[1]:
                    res.append(i+j)

        if length == 3:
            for i in tmp[0]:
                for j in tmp[1]:
                    for k in tmp[2]:
                        res.append(i+j+k)

        if length == 4:
            for i in tmp[0]:
                for j in tmp[1]:
                    for k in tmp[2]:
                        for l in tmp[3]:
                            res.append(i+j+k+l)

        return res

# @lc code=end
