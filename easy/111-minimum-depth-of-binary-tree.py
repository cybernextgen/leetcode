import unittest
from utils.tree_node import TreeNode
from typing import Optional

data = (
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 2),
    (
        TreeNode(
            2,
            None,
            TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6)))),
        ),
        5,
    ),
    (TreeNode(1, TreeNode(2)), 2),
)


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.minDepth(input_data))


if __name__ == "__main__":
    unittest.main()
