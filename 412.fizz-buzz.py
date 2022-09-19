#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# 8/8 cases passed (88 ms)
# Your runtime beats 18.92 % of python3 submissions
# Your memory usage beats 17.68 % of python3 submissions (15.3 MB)

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a = []
        for i in range(n):
            i += 1
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            if s == "":
                s += str(i)
            a.append(s)
        return a        
# @lc code=end
