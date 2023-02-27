import unittest
from utils.list_node import ListNode, linked_list_to_values_list


data = ((ListNode(4, ListNode(5, ListNode(1, ListNode(9)))), [5, 1, 9]),)


class Solution:
    def deleteNode(self, node: ListNode):
        prev_node = node
        current_node = node.next
        while current_node:
            prev_node.val = current_node.val
            if not current_node.next:
                prev_node.next = None
                break
            prev_node = current_node
            current_node = current_node.next


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for head, expected in data:
            s.deleteNode(head)
            self.assertListEqual(expected, linked_list_to_values_list(head))


if __name__ == "__main__":
    unittest.main()
