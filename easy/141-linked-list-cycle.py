import unittest
from utils.list_node import ListNode
from typing import Optional


n1 = ListNode(1)
n2 = ListNode(2)
n1.next = n2
n2.next = n1

data = ((ListNode(1, ListNode(2)), False), (n1, True))


class Solution:
    """
    O(n) memory solution
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        visited_nodes = set()
        while head:
            if head in visited_nodes:
                return True
            visited_nodes.add(head)
            head = head.next
        return False


class Solution2:
    """
    O(1) memory solution
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        while head:
            if head.next == head:
                return True
            next_head = head.next
            head.next = head
            head = next_head
        return False


class Solution3:
    """
    O(1) memory solution
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        while head:
            if getattr(head, "visited", False):
                return True
            setattr(head, "visited", True)
            head = head.next
        return False


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution3()

        for head, expected in data:
            self.assertEqual(expected, s.hasCycle(head))


if __name__ == "__main__":
    unittest.main()
