import unittest
from utils.tree_node import TreeNode
from typing import Optional

data = (
    (TreeNode(10, TreeNode(6), TreeNode(4)), True),
    (TreeNode(5, TreeNode(3), TreeNode(1)), False),
)


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if not root or not root.left or not root.right:
            return False

        return (root.left.val + root.right.val) == root.val


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for root, expected in data:
            self.assertEqual(expected, s.checkTree(root))


if __name__ == "__main__":
    unittest.main()
