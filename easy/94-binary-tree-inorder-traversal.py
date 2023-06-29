import unittest
from utils.tree_node import TreeNode
from typing import Optional, List

data = (
    (TreeNode(1, None, TreeNode(2, TreeNode(3), None)), [1, 3, 2]),
    (None, []),
    (TreeNode(1), [1]),
)


class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.inorderTraversal(root.left)
        self.result.append(root.val)
        self.inorderTraversal(root.right)
        return self.result


class TestCase(unittest.TestCase):
    def test_solution(self):
        for input_data, expected in data:
            s = Solution()
            self.assertListEqual(s.inorderTraversal(input_data), expected)


if __name__ == "__main__":
    unittest.main()
