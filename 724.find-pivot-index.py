#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)

        for i in range(len(nums)):
            r -= nums[i]
            if l == r:
                return i
            l += nums[i]
        return -1


# @lc code=end
