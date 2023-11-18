class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int, seen: Optional[Set[int]] = None) -> bool:
        if not seen:
            seen = set()
            
        if not root:
            return False
    
        current_node_val = root.val
        required_number = k - current_node_val
        result = required_number in seen
        seen.add(current_node_val)
        return result or self.findTarget(root.left, k, seen) or self.findTarget(root.right, k, seen)
