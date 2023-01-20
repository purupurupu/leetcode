#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # try:
        #     index = nums.index(target)
        #     return index

        # except:
        #     return -1

        # binary search
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# input = "abcabcbb"
input = [4, 5, 6, 7, 0, 1, 2]
target = 0


tmp = Solution()
res = tmp.search(input, target)

print(res)

# @lc code=end
