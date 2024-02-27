# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(current, prev=None):
            if not current:
                return prev
            next_node = current.next
            current.next = prev
            return helper(next_node, current)

        return helper(head)
