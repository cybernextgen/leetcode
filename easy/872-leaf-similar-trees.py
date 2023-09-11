import unittest
from utils.tree_node import TreeNode
from typing import Optional, List

data = (
    # (
    #     TreeNode(1, TreeNode(2), TreeNode(3)),
    #     TreeNode(3, TreeNode(2), TreeNode(3)),
    #     True,
    # ),
    (
        TreeNode(1, TreeNode(2), TreeNode(3)),
        TreeNode(3, TreeNode(3), TreeNode(2)),
        False,
    ),
)


def extract_tree_leafs(root: Optional[TreeNode], result: List[int] = []) -> List[int]:
    if not root:
        return result

    if not root.left and not root.right:
        result.append(root.val)
        return result

    extract_tree_leafs(root.left, result)
    extract_tree_leafs(root.right, result)
    return result


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs_1 = extract_tree_leafs(root1, [])
        leafs_2 = extract_tree_leafs(root2, [])

        if len(leafs_1) != len(leafs_2):
            return False

        for index in range(len(leafs_1)):
            if leafs_1[index] != leafs_2[index]:
                return False

        return True


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for root1, root2, expected in data:
            self.assertEqual(expected, s.leafSimilar(root1, root2))


if __name__ == "__main__":
    unittest.main()
