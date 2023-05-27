import unittest
from utils.tree_node import TreeNode
from typing import Optional

data = (
    (
        TreeNode(
            10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))
        ),
        7,
        15,
        32,
    ),
    (
        TreeNode(
            10,
            TreeNode(5, TreeNode(3, TreeNode(1)), TreeNode(7, TreeNode(6))),
            TreeNode(15, TreeNode(13), TreeNode(18)),
        ),
        6,
        10,
        23,
    ),
)


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result = 0
        if root.val > low:
            result += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            result += self.rangeSumBST(root.right, low, high)
        if low <= root.val <= high:
            result += root.val
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, low, high, expected in data:
            self.assertEqual(s.rangeSumBST(input_data, low, high), expected)


if __name__ == "__main__":
    unittest.main()
