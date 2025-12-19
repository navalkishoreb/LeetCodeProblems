# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
head → … → C → … → M → … →
          ↑             ↓
          ← ← ← ← ← ← ←
Where:
C = cycle start
M = meeting point of slow & fast

Define: distance --> count edges
a = distance from head → C
b = distance from C → M
c = length of the cycle


Since fast moves twice as fast:
fast = 2 × slow

Substitute distance travelled:
a + b + k·c = 2(a + b)

Rearrange:
a = k·c − b

Critical Insight
From the equation:
a = k·c − b


Interpretation:
Starting at M, if you move forward (c − b) steps, you reach C
Since k·c is full cycles, distance (k·c − b) also lands on C

Distance from meeting point to cycle start = distance from head to cycle start
"""


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        cycle = False
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle = True
                break
        else:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
