import unittest
from utils.list_node import ListNode
from typing import Optional

data = (
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3),
    (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))), 4),
)


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        middle_pointer = head
        tail_pointer = head
        while True:
            if not tail_pointer.next:
                return middle_pointer
            if not tail_pointer.next.next:
                return middle_pointer.next  # type: ignore

            tail_pointer = tail_pointer.next.next
            middle_pointer = middle_pointer.next  # type: ignore


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            result = s.middleNode(input_data)
            if result:
                self.assertEqual(result.val, expected)


if __name__ == "__main__":
    unittest.main()
