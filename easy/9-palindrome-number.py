import unittest

data = ((121, True), (-121, False), (10, False))


class Solution1:
    def isPalindrome(self, x: int) -> bool:
        test_string = str(x)
        for index, char in enumerate(test_string):
            if char != test_string[-index - 1]:
                return False
        return True


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        test_string = str(x)
        return test_string == test_string[::-1]


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution2()

        for input_data, result in data:
            self.assertEqual(result, s.isPalindrome(input_data))


if __name__ == "__main__":
    unittest.main()
