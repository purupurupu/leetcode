#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hl = len(haystack)
        nl = len(needle)

        for i in range(0, hl-nl+1):
            if haystack[i:i+nl] == needle:
                return i
        return -1
        # @lc code=end
