from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    """
    Trivial slow solution
    """

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = self.__produce_number_from_list_node(l1)
        num2 = self.__produce_number_from_list_node(l2)
        return self.__produce_list_node_from_num(num1 + num2)

    def __produce_number_from_list_node(self, list_node: Optional[ListNode]) -> int:
        result_str = ""
        while list_node:
            result_str = "{}{}".format(list_node.val, result_str)
            list_node = list_node.next
        return int(result_str)

    def __produce_list_node_from_num(self, num: int) -> Optional[ListNode]:
        first_node = None
        prev_node = None
        num_as_str = str(num)
        for ch in reversed(num_as_str):
            current_node = ListNode()
            current_node.val = int(ch)
            if not first_node:
                first_node = current_node
            elif prev_node:
                prev_node.next = current_node
            prev_node = current_node
        return first_node


class Solution2:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        addition = 0
        first_result_node = None
        prev_result_node = None
        while l1 or l2 or addition:
            current_result_node = ListNode()
            l1val = 0
            l2val = 0

            if l1:
                l1val = l1.val
                l1 = l1.next
            if l2:
                l2val = l2.val
                l2 = l2.next

            sum = l1val + l2val + addition
            if sum >= 10:
                addition = 1
                current_result_node.val = sum % 10
            else:
                addition = 0
                current_result_node.val = sum
            if not first_result_node:
                first_result_node = current_result_node
            elif prev_result_node:
                prev_result_node.next = current_result_node
            prev_result_node = current_result_node
        return first_result_node


if __name__ == "__main__":
    unittest.main()
