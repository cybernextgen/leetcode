import unittest
from utils.tree_node import TreeNode
from typing import Optional, Tuple

data = (
    (TreeNode(1, TreeNode(2), TreeNode(3)), 1),
    (
        TreeNode(
            4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, None, TreeNode(7))
        ),
        15,
    ),
)


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total_sum, total_tilt = self.dfs(root)
        return total_tilt

    def dfs(self, node: TreeNode) -> Tuple[int, int]:
        if node.left:
            left_sum, left_tilt = self.dfs(node.left)
        else:
            left_sum = left_tilt = 0

        if node.right:
            right_sum, right_tilt = self.dfs(node.right)
        else:
            right_sum = right_tilt = 0

        current_sum = node.val + left_sum + right_sum
        current_tilt = left_tilt + right_tilt + abs(left_sum - right_sum)

        return (current_sum, current_tilt)


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.findTilt(input_data), expected)


if __name__ == "__main__":
    unittest.main()
