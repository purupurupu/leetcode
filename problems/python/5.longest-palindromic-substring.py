#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        tmp = ""
        res = ""
        length = 0

        for i in range(len(s)):
            tmp = ""
            if len(s)-i < length and res != 0:
                return res

            for j in range(i, len(s)):
                tmp = s[i:j+1]
                reversed_s = tmp[::-1]

                if tmp == reversed_s and length < len(tmp):
                    length = len(tmp)
                    res = tmp

        return res
        # @lc code=end
