import unittest
from utils.tree_node import TreeNode
from typing import Optional

data = (
    (TreeNode(5, TreeNode(2, TreeNode(7), TreeNode(6)), TreeNode(3)), 14, True),
    (TreeNode(5, TreeNode(2, TreeNode(7), TreeNode(6)), TreeNode(3)), 16, False),
    (None, 0, False),
    (TreeNode(1, TreeNode(2)), 1, False),
)


class Solution:
    def hasPathSum(
        self,
        root: Optional[TreeNode],
        targetSum: int,
        current_sum: int = 0,
    ) -> bool:
        if not root:
            return False

        current_sum += root.val
        if not root.left and not root.right:
            return current_sum == targetSum

        else:
            return self.hasPathSum(
                root.left, targetSum, current_sum
            ) or self.hasPathSum(root.right, targetSum, current_sum)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, target, expected in data:
            self.assertEqual(expected, s.hasPathSum(input_data, target))


if __name__ == "__main__":
    unittest.main()
