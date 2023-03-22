import unittest
from utils.list_node import ListNode, linked_list_to_values_list
from typing import Optional

data = ((ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), [4, 3, 2, 1]),)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        prev_node = head
        head = prev_node.next
        prev_node.next = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            result = s.reverseList(input_data)
            self.assertListEqual(expected, linked_list_to_values_list(result))


if __name__ == "__main__":
    unittest.main()
