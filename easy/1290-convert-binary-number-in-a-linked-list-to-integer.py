import unittest
from utils.list_node import ListNode
from typing import Optional

data = ((ListNode(1, ListNode(0, ListNode(1))), 5), (ListNode(0), 0))


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        digits = str(head.val)
        while head.next:
            head = head.next
            digits += str(head.val)
        return int(digits, base=2)


class Solution2:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        while head:
            result = result * 2 + head.val
            head = head.next
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution2()

        for input_data, expected in data:
            self.assertEqual(s.getDecimalValue(input_data), expected)


if __name__ == "__main__":
    unittest.main()
