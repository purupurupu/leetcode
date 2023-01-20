#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        s = re.findall('^[+\-]?\d+', s)
        # 先頭から最初に引っかかったやつだけ出力すればOKなので、、

        try:
            res = int(''.join(s))
            MAX = 2147483647
            MIN = -2147483648
            if res > MAX:
                return MAX
            if res < MIN:
                return MIN
            return res
        except:
            return 0
            # @lc code=end
