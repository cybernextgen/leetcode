import unittest
from typing import List, Optional
from utils.tree_node import TreeNode

data = (
    (TreeNode(1, None, TreeNode(2, TreeNode(3))), [3, 2, 1]),
    (TreeNode(1), [1]),
    (None, []),
)


class Solution:
    def __init__(self) -> None:
        self.result = []

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.result.append(root.val)
        return self.result


class TestCase(unittest.TestCase):
    def test_solution(self):
        for input_data, expected in data:
            s = Solution()
            self.assertListEqual(s.postorderTraversal(input_data), expected)


if __name__ == "__main__":
    unittest.main()
