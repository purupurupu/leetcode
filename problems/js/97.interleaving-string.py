#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     print(s1, s2, s3)
    #     if len(s1) + len(s2) != len(s3):
    #         return False
    #     if len(s1) == 0:
    #         return s2 == s3
    #     if len(s2) == 0:
    #         return s1 == s3
    #     if s1[0] == s3[0]:
    #         return self.isInterleave(s1[1:], s2, s3[1:])
    #     if s2[0] == s3[0]:
    #         return self.isInterleave(s1, s2[1:], s3[1:])
    #     return False
    
    # This solution is limit exceeded
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    #     if len(s1) + len(s2) != len(s3):
    #         return False
    #     if len(s1) == 0:
    #         return s2 == s3
    #     if len(s2) == 0:
    #         return s1 == s3
    #     if s1[0] == s3[0] and s2[0] == s3[0]:
    #         return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
    #     elif s1[0] == s3[0]:
    #         return self.isInterleave(s1[1:], s2, s3[1:])
    #     elif s2[0] == s3[0]:
    #         return self.isInterleave(s1, s2[1:], s3[1:])
    #     return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(1, len(s1) + 1): 
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[len(s1)][len(s2)]
    
# @lc code=end

s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(s.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
