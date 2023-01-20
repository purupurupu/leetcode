#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # idnex setup
        left = 0
        right = len(height) - 1
        tmp = 0
        max_container = 0

        while left != right:
            tmp = (right - left) * min(height[left], height[right])
            # print(left)
            # print(right)

            if max_container < tmp:
                max_container = tmp

            if height[left] < height[right]:
                left += 1

            elif height[left] >= height[right]:
                right -= 1

            # print(left)
            # print(right)
        return max_container  # @lc code=end
