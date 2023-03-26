import unittest
from typing import Optional


class MyStack:
    def __init__(self):
        self.__elements = []

    def push(self, x: int) -> None:
        self.__elements.append(x)

    def pop(self) -> Optional[int]:
        if self.__elements:
            return self.__elements.pop()
        return None

    def top(self) -> Optional[int]:
        if self.__elements:
            return self.__elements[-1]
        return None

    def empty(self) -> bool:
        return not bool(self.__elements)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = MyStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.empty(), False)
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.empty(), True)


if __name__ == "__main__":
    unittest.main()
