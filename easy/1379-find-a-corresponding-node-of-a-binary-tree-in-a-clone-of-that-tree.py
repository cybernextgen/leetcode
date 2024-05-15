from utils.tree_node import TreeNode


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode | None, target: TreeNode
    ) -> TreeNode | None:
        if not cloned:
            return None

        if target.val == cloned.val:
            return cloned

        return self.getTargetCopy(original, cloned.left, target) or self.getTargetCopy(
            original, cloned.right, target
        )
