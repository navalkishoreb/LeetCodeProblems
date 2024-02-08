from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result = ListNode()

        def summation(a, b, carry, current_result):
            if a is None and b is None and carry == 0:
                return

            current_sum = carry

            if a:
                current_sum += a.val
                a = a.next
            if b:
                current_sum += b.val
                b = b.next

            result_node = ListNode(val=current_sum % 10)
            carry = current_sum // 10
            current_result.next = result_node
            current_result = result_node
            summation(a, b, carry, current_result)

        summation(l1, l2, 0, result)
        return result.next
