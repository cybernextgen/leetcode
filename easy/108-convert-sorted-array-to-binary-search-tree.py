import unittest
from typing import List, Optional
from utils.tree_node import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        len_nums = len(nums)
        if not len_nums:
            return None
        current_index = len_nums // 2
        current_node = TreeNode(nums[current_index])
        current_node.left = self.sortedArrayToBST(nums[:current_index])
        current_node.right = self.sortedArrayToBST(nums[current_index + 1 :])
        return current_node
