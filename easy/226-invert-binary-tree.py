import unittest
from typing import Optional
from utils.tree_node import TreeNode

data = (
    (
        TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        ),
        TreeNode(
            4,
            TreeNode(7, TreeNode(9), TreeNode(6)),
            TreeNode(2, TreeNode(3), TreeNode(1)),
        ),
    ),
)


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p and not q or q and not p:
        return False
    if not p and not q:
        return True
    return (
        is_same_tree(p.left, q.left)  # type: ignore
        and is_same_tree(p.right, q.right)  # type: ignore
        and p.val == q.val  # type: ignore
    )


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for tree1, tree2 in data:
            inverted_tree = s.invertTree(tree1)
            self.assertTrue(is_same_tree(inverted_tree, tree2))


if __name__ == "__main__":
    unittest.main()
