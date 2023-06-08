import unittest
import itertools

data = (
    ("aaaaaaaa", ""),
    ("abbaca", "ca"),
    ("azxxzy", "ay"),
)


class Solution:
    def removeDuplicates(self, s: str) -> str:
        prev_char = ""
        for index, char in enumerate(s):
            if char == prev_char:
                return self.removeDuplicates(s[: index - 1] + s[index + 1 :])
            prev_char = char
        return s


class Solution2:
    def removeDuplicates(self, s: str) -> str:
        chars_list = list(s)
        index = 0
        prev_char = ""
        while index < len(chars_list):
            current_char = chars_list[index]

            if current_char != prev_char:
                prev_char = current_char
                index += 1
                continue

            del chars_list[index]
            if index >= 1:
                index -= 1
                del chars_list[index]

            if index > 0:
                prev_char = chars_list[index - 1]
            else:
                prev_char = ""

        return "".join(chars_list)


class Solution3:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution3()
        for input_data, result in data:
            self.assertEqual(s.removeDuplicates(input_data), result)


if __name__ == "__main__":
    unittest.main()
