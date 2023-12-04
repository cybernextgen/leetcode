import unittest

data = (("string", "rtsng"), ("poiinter", "ponter"))


class Solution:
    def finalString(self, s: str) -> str:
        result = ""
        for ch in s:
            if ch == "i":
                result = result[::-1]
            else:
                result += ch
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for original, expected in data:
            self.assertEqual(expected, s.finalString(original))


if __name__ == "__main__":
    unittest.main()
