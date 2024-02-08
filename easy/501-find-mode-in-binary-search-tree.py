import unittest
from typing import Optional, List
from utils.tree_node import TreeNode
import collections

data = ((TreeNode(1, None, TreeNode(2, TreeNode(2))), [2]), (TreeNode(0), [0]))


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        serialized_tree = []
        self.__traverse_tree(root, serialized_tree)
        counts = collections.Counter(serialized_tree)
        max_count = max(counts.values())
        return [key for key, val in counts.items() if val == max_count]

    def __traverse_tree(self, node: Optional[TreeNode], serialized_tree: List[int]):
        if not node:
            return
        self.__traverse_tree(node.left, serialized_tree)
        self.__traverse_tree(node.right, serialized_tree)
        serialized_tree.append(node.val)


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertListEqual(s.findMode(input_data), expected)


if __name__ == "__main__":
    unittest.main()
