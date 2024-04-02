import unittest
from typing import List

data = (
    ([1, 2, 3], [1, 1], 1),
    ([1, 2], [1, 2, 3], 2),
)


class Solution:
    def findContentChildren(self, childs: List[int], cookies: List[int]) -> int:
        childs.sort()
        cookies.sort()
        cookie_index = child_index = 0
        while cookie_index < len(cookies) and child_index < len(childs):
            if cookies[cookie_index] >= childs[child_index]:
                child_index += 1
            cookie_index += 1
        return child_index


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for g, cookies, expected in data:
            self.assertEqual(expected, s.findContentChildren(g, cookies))


if __name__ == "__main__":
    unittest.main()
