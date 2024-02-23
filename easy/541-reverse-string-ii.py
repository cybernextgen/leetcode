import unittest

data = (("abcdefg", 2, "bacdfeg"), ("abcd", 2, "bacd"))


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        reverse = True
        result = ""
        for index in range(0, len(s), k):

            sub = s[index : index + k]
            if reverse:
                result += sub[::-1]
            else:
                result += sub
            reverse = not reverse
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_str, k, expected in data:
            self.assertEqual(s.reverseStr(input_str, k), expected)


if __name__ == "__main__":
    unittest.main()
