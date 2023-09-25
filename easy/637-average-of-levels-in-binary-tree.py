import unittest
from utils.tree_node import TreeNode
from typing import List, Optional, Tuple, Dict

data = (
    (TreeNode(5, TreeNode(2), TreeNode(-3)), [5.00000, -0.50000]),
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), [3, 14.5, 11]),
    (TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20)), [3, 14.5, 11]),
)


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        levels_stats = self.__get_levels_stats(root, [])
        return [
            levels_stats[i][0] / levels_stats[i][1] for i in range(0, len(levels_stats))
        ]

    def __get_levels_stats(
        self,
        root: TreeNode,
        levels_stats: List[List[int]],
        current_level=0,
    ) -> List[List[int]]:
        if not levels_stats or len(levels_stats) == current_level:
            levels_stats.append([root.val, 1])
        else:
            levels_stats[current_level][0] += root.val
            levels_stats[current_level][1] += 1

        if root.left:
            self.__get_levels_stats(root.left, levels_stats, current_level + 1)
        if root.right:
            self.__get_levels_stats(root.right, levels_stats, current_level + 1)

        return levels_stats


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for root, expected in data:
            self.assertListEqual(expected, s.averageOfLevels(root))


if __name__ == "__main__":
    unittest.main()
