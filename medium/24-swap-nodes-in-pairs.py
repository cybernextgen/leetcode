import unittest
from typing import Optional
from utils.list_node import ListNode, linked_list_to_values_list


data = (
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), [2, 1, 4, 3]),
    (ListNode(1), [1]),
)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        first_node = head
        while next := head.next:
            if not prev:
                prev = head
            else:
                prev.val, head.val = head.val, prev.val
                prev = None
            head = next

        if prev:
            prev.val, head.val = head.val, prev.val

        return first_node


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(
                expected, linked_list_to_values_list(s.swapPairs(input_data))
            )


if __name__ == "__main__":
    unittest.main()
