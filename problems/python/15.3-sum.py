#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        s = 0

        for i, j in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # j is left pointer , k is right pointer
            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1  # skip equal prev case
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1  # skip equal prev case
        return res
        # @lc code=end
