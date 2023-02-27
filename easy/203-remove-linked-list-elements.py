import unittest
from typing import Optional
from utils.list_node import ListNode, LinkedListIterator, linked_list_to_values_list

data = (
    # (
    #     ListNode(
    #         1,
    #         ListNode(
    #             2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
    #         ),
    #     ),
    #     6,
    #     [1, 2, 3, 4, 5],
    # ),
    (None, 1, []),
    (ListNode(7, ListNode(7, ListNode(7, ListNode(7)))), 7, []),
)


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        result_head: Optional[ListNode] = None
        prev_element: Optional[ListNode] = None
        current_element: ListNode = head
        while current_element:
            if current_element.val != val:
                if not result_head:
                    result_head = current_element
                if prev_element:
                    prev_element.next = current_element
                prev_element = current_element
            current_element = current_element.next  # type: ignore

        if prev_element:
            prev_element.next = None
        return result_head


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_list, removed_val, expected in data:
            result = s.removeElements(input_list, removed_val)
            self.assertListEqual(expected, linked_list_to_values_list(result))


if __name__ == "__main__":
    unittest.main()
