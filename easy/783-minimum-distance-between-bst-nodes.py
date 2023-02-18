from utils.tree_node import TreeNode
from typing import Optional, List
import unittest
from itertools import combinations
import sys

data = (
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6)), 1),
    (TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49))), 1),
)


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min_distance = sys.maxsize
        self.prev_node_val = -(sys.maxsize - 1)
        self.__visit_node(root)
        return self.min_distance

    def __visit_node(self, node: Optional[TreeNode]) -> None:
        if not node:
            return
        self.__visit_node(node.left)
        current_distance = node.val - self.prev_node_val
        self.min_distance = min(self.min_distance, current_distance)
        self.prev_node_val = node.val
        self.__visit_node(node.right)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.minDiffInBST(input_data))


if __name__ == "__main__":
    unittest.main()
