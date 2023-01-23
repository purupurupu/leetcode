#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
import itertools
from typing import List

# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        p = itertools.permutations(nums, len(nums))
        return p

# @lc code=end
