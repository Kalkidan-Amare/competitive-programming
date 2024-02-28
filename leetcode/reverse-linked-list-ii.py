# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        temp = dummy
        for i in range(1, left):
            temp = temp.next

        prev = None
        curr = temp.next
        for i in range(left, right + 1):
            nextN = curr.next
            curr.next = prev
            prev = curr
            curr = nextN

        temp.next.next = curr
        temp.next = prev

        return dummy.next
