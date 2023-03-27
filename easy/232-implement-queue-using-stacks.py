import unittest
from typing import List


class MyQueue:
    def __init__(self):
        self.__elements: List[int] = []

    def push(self, x: int) -> None:
        self.__elements.append(x)

    def pop(self) -> int:
        element = self.__elements[0]
        del self.__elements[0]
        return element

    def peek(self) -> int:
        return self.__elements[0]

    def empty(self) -> bool:
        return not bool(self.__elements)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = MyQueue()
        s.push(1)
        s.push(2)
        self.assertEqual(s.empty(), False)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.empty(), True)


if __name__ == "__main__":
    unittest.main()
