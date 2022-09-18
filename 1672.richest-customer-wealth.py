#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a = 0
        for ac in accounts:
            gt = 0
            for m in ac:
                gt += m
                if a < gt:
                    a = gt
        return a
# @lc code=end

