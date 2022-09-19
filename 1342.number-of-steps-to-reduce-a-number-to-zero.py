#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#
# 204/204 cases passed (39 ms)
# Your runtime beats 77.84 % of python3 submissions
# Your memory usage beats 8.04 % of python3 submissions (13.9 MB)

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        a = 0
        while num > 0:
            if num & 1 == 0:
                # odd
                num >>= 1
            else:
                # even
                num -= 1
            a += 1
        return a
# @lc code=end
