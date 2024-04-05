import unittest
from utils.tree_node import TreeNode
from typing import Optional, List, Tuple

data = (
    (
        TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5)),
        TreeNode(4, TreeNode(1), TreeNode(2)),
        True,
    ),
    (
        TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5)),
        TreeNode(4, TreeNode(1), TreeNode(2)),
        False,
    ),
)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
        serialized_subtree = self.__serialize_tree(sub_root)
        return self.__check_subtree(root, serialized_subtree)[0]

    def __serialize_tree(self, node: TreeNode | None) -> List[Optional[int]]:
        if not node:
            return [None]
        result = (
            [node.val]
            + self.__serialize_tree(node.left)
            + self.__serialize_tree(node.right)
        )
        return result

    def __check_subtree(
        self, node: Optional[TreeNode], serialized_subtree: List[Optional[int]]
    ) -> Tuple[bool, List[Optional[int]]]:
        if not node:
            return (False, [None])

        is_left_has_subtree, left_path = self.__check_subtree(
            node.left, serialized_subtree
        )
        is_right_has_subtree, right_path = self.__check_subtree(
            node.right, serialized_subtree
        )

        path = [node.val] + left_path + right_path
        has_subtree = (
            is_left_has_subtree or is_right_has_subtree or path == serialized_subtree
        )
        return (has_subtree, path)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for root, sub_root, expected in data:
            self.assertEqual(s.isSubtree(root, sub_root), expected)


if __name__ == "__main__":
    unittest.main()
