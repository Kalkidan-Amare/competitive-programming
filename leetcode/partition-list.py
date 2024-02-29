# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        lessDummy = ListNode()
        greatDummy = ListNode()
        less = lessDummy
        great = greatDummy

        while temp:
            if temp.val < x:
                less.next = temp
                less = less.next
            else:
                great.next = temp
                great = great.next
            temp = temp.next
        great.next = None
        less.next = greatDummy.next

        return lessDummy.next
        
        