import unittest
from typing import Optional, List
from utils.tree_node import TreeNode

data = (
    (TreeNode(1, None, TreeNode(2, TreeNode(3))), [1, 2, 3]),
    (None, []),
    (TreeNode(1), [1]),
)


class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.result.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.result


class TestCase(unittest.TestCase):
    def test_solution(self):
        for input_data, expected in data:
            s = Solution()
            self.assertListEqual(s.preorderTraversal(input_data), expected)


if __name__ == "__main__":
    unittest.main()
