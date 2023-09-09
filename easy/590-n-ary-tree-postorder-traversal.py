import unittest
from typing import List, Optional


class Node:
    def __init__(self, val=None, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.result = []

    def postorder(self, root: Node) -> List[int]:
        if not root:
            return []

        if root.children:
            for n in root.children:
                self.postorder(n)

        self.result.append(root.val)
        return self.result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        tree = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        self.assertListEqual([5, 6, 3, 2, 4, 1], s.postorder(tree))


if __name__ == "__main__":
    unittest.main()
