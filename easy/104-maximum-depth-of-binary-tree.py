import unittest
from typing import Optional
from utils.tree_node import TreeNode

data = (
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 3),
    (TreeNode(1, None, TreeNode(2)), 2),
)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        current_depth = 0
        for child in (root.left, root.right):
            depth_from_child = self.maxDepth(child)
            if depth_from_child > current_depth:
                current_depth = depth_from_child
        current_depth += 1
        return current_depth


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.maxDepth(input_data))


if __name__ == "__main__":
    unittest.main()
