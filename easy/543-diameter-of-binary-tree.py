import unittest
from utils.tree_node import TreeNode
from typing import Optional

data = (
    (TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)), 3),
    (TreeNode(1, TreeNode(2)), 1),
)


class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.__search_diameter(root)
        return self.result

    def __search_diameter(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_height = self.__search_diameter(node.left)
        right_height = self.__search_diameter(node.right)
        self.result = max(self.result, left_height + right_height)
        return max(left_height, right_height) + 1


class TestCase(unittest.TestCase):
    def test_solution(self):
        for input_data, expected in data:
            s = Solution()
            self.assertEqual(s.diameterOfBinaryTree(input_data), expected)


if __name__ == "__main__":
    unittest.main()
