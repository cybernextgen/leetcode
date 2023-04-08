import unittest
from typing import List, Optional
from utils.tree_node import TreeNode

data = (
    (TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3)), ["1->2->5", "1->3"]),
    (TreeNode(1), ["1"]),
    (
        TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),
        ["1->2->4", "1->2->5", "1->3"],
    ),
)


class Solution:
    def binaryTreePaths(
        self, root: Optional[TreeNode], current_path: str = ""
    ) -> List[str]:
        if not root:
            return []

        if current_path:
            current_path = f"{current_path}->{root.val}"
        else:
            self.paths = []
            current_path = str(root.val)

        if not root.left and not root.right:
            self.paths.append(current_path)
        else:
            self.binaryTreePaths(root.left, current_path)
            self.binaryTreePaths(root.right, current_path)
        return self.paths


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertListEqual(result, s.binaryTreePaths(input_data))


if __name__ == "__main__":
    unittest.main()
