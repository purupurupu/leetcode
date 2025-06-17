#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        nums.sort(reverse=True)
        return nums[2]

# @lc code=end

solution = Solution()

print(solution.thirdMax([3,2,1]))
print(solution.thirdMax([1,2]))
print(solution.thirdMax([2,2,3,1]))
