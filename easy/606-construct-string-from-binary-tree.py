import unittest
from utils.tree_node import TreeNode
from typing import Optional

data = (
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(4)),
            TreeNode(3),
        ),
        "1(2(4))(3)",
    ),
    (
        TreeNode(
            1,
            TreeNode(2, None, TreeNode(4)),
            TreeNode(3),
        ),
        "1(2()(4))(3)",
    ),
)


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = f"{root.val}"

        if root.right:
            result += f"({self.tree2str(root.left)})({self.tree2str(root.right)})"
        elif root.left:
            result += f"({self.tree2str(root.left)})"

        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.tree2str(input_data), input_data)


if __name__ == "__main__":
    unittest.main()
