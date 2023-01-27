#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from typing import List
# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resList = []
        sortList = []
        for v in strs:
            sortList.append("".join(sorted(v)))

        distList = list(set(sortList))

        for c in distList:
            tmpList = []
            count = sortList.count(c)
            start = 0
            for n in range(count):
                index = sortList[start:].index(c) + start
                tmpList.append(strs[index])
                start = index + 1
            resList.append(tmpList)

        return (resList)

        # @lc code=end
