from typing import Optional
from utils.list_node import ListNode
import unittest

tail = ListNode(8, ListNode(4, ListNode(5)))

headA = ListNode(4, ListNode(1, tail))
headB = ListNode(5, ListNode(6, ListNode(1, tail)))


class Solution:
    def getIntersectionNode(
        self, headA: Optional[ListNode], headB: Optional[ListNode]
    ) -> Optional[ListNode]:
        seen = set()
        result = None
        vars = [headA, headB]
        while True:
            if not any(vars):
                break
            for index, var in enumerate(vars):
                if var:
                    if var not in seen:
                        seen.add(var)
                        vars[index] = var.next
                    else:
                        return var

        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(tail, s.getIntersectionNode(headA, headB))


if __name__ == "__main__":
    unittest.main()
