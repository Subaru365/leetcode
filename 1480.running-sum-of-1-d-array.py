#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a = []
        m = 0
        for n in nums:
            a.append(m+n)
            m+=n
        return a
# @lc code=end
