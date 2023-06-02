import unittest
from utils.tree_node import TreeNode
from typing import Optional

data = (
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), 4, 3, False),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5))), 5, 4, True),
    (TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3)), 2, 3, False),
)


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        self.found_nodes = []
        self.target_values = set([x, y])
        self.__find_nodes(root, 0)
        assert len(self.found_nodes) == 2
        first_found_node = self.found_nodes[0]
        second_found_node = self.found_nodes[1]
        return (
            first_found_node[0] != second_found_node[0]
            and first_found_node[1] == second_found_node[1]
        )

    def __find_nodes(
        self,
        node: Optional[TreeNode],
        parent_value: int,
        current_depth=0,
    ) -> None:
        if not node:
            return
        current_depth += 1
        if node.val in self.target_values:
            self.found_nodes.append((parent_value, current_depth))

        if len(self.found_nodes) == 2:
            return

        self.__find_nodes(node.left, node.val, current_depth)
        self.__find_nodes(node.right, node.val, current_depth)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, x, y, expected in data:
            self.assertEqual(s.isCousins(input_data, x, y), expected)


if __name__ == "__main__":
    unittest.main()
