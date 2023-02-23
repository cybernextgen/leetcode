import unittest
from typing import List

data = (
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["ab", "a"], "a"),
    (["abab", "aba", ""], ""),
)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        min_length = min([len(s) for s in strs])
        if not min_length:
            return ""

        index = 0
        for index in range(min_length):
            current_char = strs[0][index]
            for s in strs[1:]:
                if current_char != s[index]:
                    return strs[0][:index]
        return strs[0][: index + 1]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(result, s.longestCommonPrefix(input_data))


if __name__ == "__main__":
    unittest.main()
