import unittest
from utils.tree_node import TreeNode
from typing import Optional

data = (
    (
        TreeNode(
            1,
            TreeNode(2, TreeNode(3), TreeNode(4)),
            TreeNode(2, TreeNode(4), TreeNode(3)),
        ),
        True,
    ),
    (
        TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(2, None, TreeNode(4))),
        False,
    ),
)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.__is_nodes_symmetric(root.left, root.right)

    def __is_nodes_symmetric(
        self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]
    ) -> bool:
        if (not left_node and right_node) or (not right_node and left_node):
            return False
        elif not left_node and not right_node:
            return True
        return (
            self.__is_nodes_symmetric(left_node.left, right_node.right)  # type: ignore
            and self.__is_nodes_symmetric(left_node.right, right_node.left)  # type: ignore
            and left_node.val == right_node.val  # type: ignore
        )


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.isSymmetric(input_data))


if __name__ == "__main__":
    unittest.main()
