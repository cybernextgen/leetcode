class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val < 2:
            return bool(root.val)
        
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        if root.val == 2:
            return left_val or right_val
        return left_val and right_val
