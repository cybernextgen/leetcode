from utils.tree_node import TreeNode
import unittest
from typing import Optional

data = (
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), 24),
    (TreeNode(1), 0),
)


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], isLeft=False) -> int:
        if not root:
            return 0

        if isLeft and not root.left and not root.right:
            return root.val

        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.sumOfLeftLeaves(input_data))


if __name__ == "__main__":
    unittest.main()
