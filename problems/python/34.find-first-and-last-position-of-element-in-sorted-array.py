#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        cnt = nums.count(target)

        if cnt == 0:
            return [-1, -1]

        index = nums.index(target)

        # if cnt == 1:
        #     return [index, index]
        # else:
        return [index, index+cnt-1]

        # other solution
        # startingPos = -1
        # endingPos = -1
        # m = len(nums)
        # if (m != 0) and (target>=nums[0]) and (target<=nums[m-1]):
        #     for i in range(m):
        #         if startingPos == -1:
        #             if nums[i] == target:
        #                 startingPos = i
        #                 endingPos = i
        #         elif nums[i] == target:
        #             endingPos = i
        #         else:
        #             break
        # return [startingPos, endingPos]


# @lc code=end
