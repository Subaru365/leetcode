#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# 36/36 cases passed (68 ms)
# Your runtime beats 7.35 % of python3 submissions
# Your memory usage beats 95.38 % of python3 submissions (13.7 MB)

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = middle = head
        while cursor and cursor.next:
            middle = middle.next
            cursor = cursor.next.next
        return middle
# @lc code=end
