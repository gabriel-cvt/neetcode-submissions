# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        slow = fast = head
        second = None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        while second:
            q.append(second)
            second = second.next
        
        runner = head
        while q:
            node = q.pop()
            node.next = runner.next
            runner.next = node
            runner = node.next