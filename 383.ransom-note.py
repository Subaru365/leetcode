#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# 127/127 cases passed (109 ms)
# Your runtime beats 38.01 % of python3 submissions
# Your memory usage beats 52.74 % of python3 submissions (14.2 MB)

# @lc code=start
import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rm = collections.Counter(ransomNote)
        mg = collections.Counter(magazine)

        for k, v in rm.items():
            if k not in mg or mg[k] < v:
                return False

        return True
# @lc code=end
