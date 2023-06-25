import unittest
from utils.tree_node import TreeNode
from typing import Optional

data = (
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 2, 2),
    (TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5, None),
)


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if val > root.val:
            return self.searchBST(root.right, val)
        if val < root.val:
            return self.searchBST(root.left, val)
        return root


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for tree, val, expected in data:
            result = s.searchBST(tree, val)
            if result:
                self.assertEqual(result.val, expected)
            else:
                self.assertEquals(result, expected)


if __name__ == "__main__":
    unittest.main()
