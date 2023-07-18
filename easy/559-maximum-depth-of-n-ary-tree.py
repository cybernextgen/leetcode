from typing import Optional, List


class Node:
    def __init__(self, val=None, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: "Node") -> int:
        if not root:
            return 0

        if not root.children:
            return 1

        return 1 + max([self.maxDepth(n) for n in root.children])
