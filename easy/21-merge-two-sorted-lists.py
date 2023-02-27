import unittest
from typing import Optional, List
from utils.list_node import ListNode, linked_list_to_values_list, LinkedListIterator
import heapq

data = (
    (
        ListNode(1, ListNode(2, ListNode(4))),
        ListNode(1, ListNode(3, ListNode(4))),
        [1, 1, 2, 3, 4, 4],
    ),
    (None, None, []),
    (None, ListNode(0), [0]),
)


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        merged_list = heapq.merge(
            LinkedListIterator(list1), LinkedListIterator(list2), key=lambda x: x.val
        )

        result_head: Optional[ListNode] = None
        prev_node: Optional[ListNode] = None
        for i in merged_list:
            current_node = ListNode(i.val)
            if not result_head:
                result_head = current_node
                prev_node = current_node
                continue
            prev_node.next = current_node  # type: ignore
            prev_node = current_node
        return result_head


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for list1, list2, expected in data:
            result = linked_list_to_values_list(s.mergeTwoLists(list1, list2))
            self.assertListEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
