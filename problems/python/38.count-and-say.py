#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
from collections import OrderedDict

# @lc code=start


class Solution:
    def stringCount(self, num: int) -> str:

        # first return point
        if num == 1:
            return '1'

        ret = ''

        # num to 1
        # first res = '1'
        tmpString = self.stringCount(num-1)

        # distString = tmpString
        distinctString = ''.join(OrderedDict.fromkeys(tmpString))

        for char in distinctString:
            count = tmpString.count(char)
            ret = ret + str(count) + char
            print(ret)

        return ret

    def countAndSay(self, n: int) -> str:

        return self.stringCount(n)
        # @lc code=end


n = 4

tmp = Solution()
res = tmp.countAndSay(n)

# print(res)


# n = 1: return 1 is the base case
# n = 2: return count of last entry i.e. 1 1
# n = 3: return count of last entry i.e. two 1's so 21
# n=4: we have one 2 and one 1 so 1211
# n=5: , we have one 1 and one 2 and two 1's so -> 111221
# n=6: we have three 1's, two 2's and one 1 so -> 312211
# n = 7: we have one 3, one 1, two 2's and two 1's -> 13112221
# ...
# n = i: return counts in front of the number for entry of i-1 case
