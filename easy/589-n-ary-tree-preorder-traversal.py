from typing import List, Optional


class Node:
    def __init__(self, val=None, children: Optional[List["Node"]] = None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.result = []

    def preorder(self, root: "Node") -> List[int]:
        if not root:
            return self.result

        self.result.append(root.val)

        if root.children:
            for node in root.children:
                self.preorder(node)
        return self.result
