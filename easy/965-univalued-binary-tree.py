import unittest
from utils.tree_node import TreeNode
from typing import Optional

data = (
    (
        TreeNode(
            1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, None, TreeNode(1))
        ),
        True,
    ),
    (TreeNode(2, TreeNode(2, TreeNode(5), TreeNode(2)), TreeNode(2)), False),
)


class Solution:
    def isUnivalTree(
        self, root: Optional[TreeNode], prev_val: Optional[int] = None
    ) -> bool:
        if not root:
            return True
        if prev_val is not None and root.val != prev_val:
            return False
        return self.isUnivalTree(root.left, root.val) and self.isUnivalTree(
            root.right, root.val
        )


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.isUnivalTree(input_data), expected)


if __name__ == "__main__":
    unittest.main()
