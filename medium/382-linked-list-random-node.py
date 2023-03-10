from utils.list_node import ListNode
from typing import Optional
import random


class Solution:
    def __init__(self, head: Optional[ListNode]):
        list_length = 0
        self.head = head
        while head:
            list_length += 1
            head = head.next
        self.list_length = list_length

    def getRandom(self) -> int:
        if not self.head:
            return 0

        random_index = random.randint(1, self.list_length)
        index = 1
        current_node = self.head
        while current_node and index < random_index:
            current_node = current_node.next
            index += 1
        if current_node:
            return current_node.val
        return 0
