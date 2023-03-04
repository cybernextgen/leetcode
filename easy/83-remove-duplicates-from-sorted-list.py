import unittest
from typing import Optional
from utils.list_node import ListNode, linked_list_to_values_list

data = (
    (ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3))))), [1, 2, 3]),
    (ListNode(1, ListNode(1, ListNode(1))), [1]),
)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        first_node = head
        prev_node: Optional[ListNode] = None
        current_node = head
        while current_node:
            if prev_node and current_node.val == prev_node.val:
                next_node = current_node.next
                prev_node.next = next_node
                current_node = next_node
                continue
            prev_node = current_node
            current_node = current_node.next
        return first_node


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            result = s.deleteDuplicates(input_data)
            self.assertListEqual(expected, linked_list_to_values_list(result))


if __name__ == "__main__":
    unittest.main()
