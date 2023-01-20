#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = maxLength = 0
        usedChar = {}
        for index, char in enumerate(s):
            # 重複が発生したらstartを重複発生地点にする。
            # 重複した地点より以降に出現した文字列であればスタート再設置
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            else:
                # 重複が発生するまで、maxLengthは更新されていくような動き。
                maxLength = max(maxLength, index - start + 1)
            usedChar[char] = index
        return maxLength
        # @lc code=end
