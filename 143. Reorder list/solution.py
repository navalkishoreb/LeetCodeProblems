# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # break at middle
        second = slow.next
        slow.next = None

        # reverse second half
        prev = None
        front = None
        while second:
            front = second.next
            second.next = prev
            prev = second
            second = front

        # merge 
        second = prev
        first = head
        while first and second:
            forward = first.next
            backward = second.next
            first.next = second
            second.next = forward
            first = forward
            second = backward
