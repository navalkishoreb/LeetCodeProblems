from typing import List

import pytest

from src.AddTwoNumbers.solution import ListNode, Solution


@pytest.mark.parametrize(
    argnames=["l1", "l2", "expected"],
    argvalues=[
        [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]],
        [[0], [0], [0]],
        [[], [], []],
        [[2, 4, 3], [5, 6, 4], [7, 0, 8]],
        list().index(),
    ],
)
@pytest.mark.timeout(1)
def test_addTwoNumbers(l1, l2, expected):
    def link_nodes(nodes: List[int]) -> ListNode:
        head = None
        if nodes:
            val = nodes.pop(0)
            head = ListNode(val=val)
            head.next = link_nodes(nodes)
        return head

    def list_nodes(head: ListNode) -> List[int]:
        result = []

        while head:
            result.append(head.val)
            head = head.next
        return result

    l1 = link_nodes(l1)
    l2 = link_nodes(l2)

    actual = Solution().addTwoNumbers(l1=l1, l2=l2)
    actual = list_nodes(actual)
    assert actual == expected
