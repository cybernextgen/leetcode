import unittest
import re

data = (("Hello, my name is John", 5), ("Hello", 1))


class Solution:
    def countSegments(self, s: str) -> int:
        return len(re.findall(r"(\S+)", s))


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.countSegments(input_data), expected)


if __name__ == "__main__":
    unittest.main()
