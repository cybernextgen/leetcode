import unittest

data = (("Hello", "hello"), ("here", "here"), ("LOVELY", "lovely"))


class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join([chr(ord(ch) + 32) if "A" <= ch <= "Z" else ch for ch in s])


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.toLowerCase(input_data), input_data)


if __name__ == "__main__":
    unittest.main()
