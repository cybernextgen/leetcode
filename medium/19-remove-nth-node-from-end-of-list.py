from typing import Optional
from utils.list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        left_pointer = head
        right_pointer = head

        for i in range(n):
            right_pointer = right_pointer.next

        if not right_pointer:
            return left_pointer.next

        while right_pointer.next:
            right_pointer = right_pointer.next
            left_pointer = left_pointer.next
        left_pointer.next = left_pointer.next.next
        return head
