from utils.tree_node import TreeNode
import unittest
from typing import List, Optional

subtree1 = TreeNode(4)
subtree2 = TreeNode(2, subtree1)
data = (
    (
        TreeNode(
            1,
            subtree2,
            TreeNode(3, subtree2, TreeNode(4)),
        ),
        [subtree1, subtree2],
    ),
)


class Solution:
    def __init__(self):
        self.result = []
        self.visited_nodes = {}
        self.prev_node_hash = ""

    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        result = []
        if not root:
            return result

        node_hash = ""
        for child, child_dir in ((root.left, "l"), (root.right, "r")):
            if child:
                result += self.findDuplicateSubtrees(child)
                node_hash += self.prev_node_hash + child_dir
                self.prev_node_hash = ""

        node_hash += str(root.val)
        self.prev_node_hash = node_hash
        visited_node = self.visited_nodes.get(node_hash)
        if visited_node:
            if visited_node["count"] == 1:
                result.append(visited_node["node"])
            visited_node["count"] += 1
        else:
            self.visited_nodes[node_hash] = {"node": root, "count": 1}
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertListEqual(s.findDuplicateSubtrees(input_data), result)


if __name__ == "__main__":
    unittest.main()
