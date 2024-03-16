from typing import Optional, List
from utils.tree_node import TreeNode


class BSTIterator:

    __stack: List[TreeNode]

    def __init__(self, root: Optional[TreeNode]):
        self.__stack = []

        if not root:
            return

        while root:
            self.__stack.append(root)
            root = root.left

    def next(self) -> int:
        current_node = self.__stack.pop()
        n = current_node.right
        while n:
            self.__stack.append(n)
            n = n.left
        return current_node.val

    def hasNext(self) -> bool:
        return len(self.__stack) > 0
