import unittest
from typing import Optional
from utils.list_node import ListNode


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

n5 = ListNode(1)
n6 = ListNode(2)
n5.next = n6
n6.next = n5

data = ((n1, n2), (n5, n5), (ListNode(1), None))


class Solution1:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        visited_nodes = set()
        while head:
            if head in visited_nodes:
                return head
            visited_nodes.add(head)
            head = head.next
        return None


class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head:
            next_node = head.next
            if next_node == head:
                return head

            head.next = head
            head = next_node
        return None


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution2()

        for input_data, result in data:
            self.assertEqual(s.detectCycle(input_data), result)


if __name__ == "__main__":
    unittest.main()
