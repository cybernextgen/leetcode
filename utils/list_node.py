from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


def linked_list_to_values_list(lst: Optional[ListNode]) -> List[int]:
    if not lst:
        return []
    result = []
    for i in LinkedListIterator(lst):
        result.append(i.val)
    return result


class LinkedListIterator:
    def __init__(self, head: ListNode) -> None:
        self.head = head

    def __iter__(self) -> "LinkedListIterator":
        return self

    def __next__(self) -> ListNode:
        if not self.head:
            raise StopIteration
        current_node = self.head
        self.head = self.head.next
        return current_node
