import unittest
from typing import Optional
from utils.tree_node import TreeNode

data = (
    (
        TreeNode(
            1,
            TreeNode(0, TreeNode(0), TreeNode(1)),
            TreeNode(1, TreeNode(0), TreeNode(1)),
        ),
        22,
    ),
    (TreeNode(0), 0),
)


class Solution:
    def __init__(self):
        self.sum = 0

    def sumRootToLeaf(self, root: Optional[TreeNode], current_bits: str = "") -> int:
        if not root:
            return 0

        current_bits = f"{current_bits}{root.val}"
        if root.left:
            self.sumRootToLeaf(root.left, current_bits)
        if root.right:
            self.sumRootToLeaf(root.right, current_bits)
        if not root.left and not root.right:
            current_root_to_leaf_value = int(current_bits, 2)
            self.sum += current_root_to_leaf_value
        return self.sum


class Solution2:
    def sumRootToLeaf(self, root: Optional[TreeNode], current_sum=0) -> int:
        if not root:
            return 0

        current_sum = current_sum * 2 + root.val
        if not root.left and not root.right:
            return current_sum
        return self.sumRootToLeaf(root.left, current_sum) + self.sumRootToLeaf(
            root.right, current_sum
        )


class Test(unittest.TestCase):
    def test_parse(self):
        for input_data, result in data:
            s = Solution2()
            self.assertEqual(s.sumRootToLeaf(input_data), result)


if __name__ == "__main__":
    unittest.main()
