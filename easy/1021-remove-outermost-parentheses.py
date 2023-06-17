import unittest

data = (("(()())(())", "()()()"), ("(()())(())(()(()))", "()()()()(())"), ("()()", ""))


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        parenthes_count = 0
        for char in s:
            if char == "(":
                parenthes_count += 1
                if parenthes_count == 1:
                    continue
            else:
                parenthes_count -= 1
                if parenthes_count == 0:
                    continue
            result += char
        return result


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for input_data, result in data:
            self.assertEqual(s.removeOuterParentheses(input_data), result)


if __name__ == "__main__":
    unittest.main()
