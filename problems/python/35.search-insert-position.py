#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        beforeFlag = False
        beforeIdx = 0

        if target < nums[0]:
            return 0

        for i, val in enumerate(nums):
            if val < target:
                beforeFlag = True
                beforeIdx = i

            if val == target:
                idx = nums.index(target)
                return idx

            if beforeFlag == True and val > target:
                beforeFlag = False
                beforeIdx = i
                return beforeIdx

        return len(nums)
# @lc code=end
