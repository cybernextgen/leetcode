import unittest

data = (
    ("G()(al)", "Goal"),
    ("G()()()()(al)", "Gooooal"),
    ("(al)G(al)()()G", "alGalooG"),
)


class Solution:
    def interpret(self, command: str) -> str:
        index = 0
        result = ""
        while index < len(command):
            current_char = command[index]
            if current_char == "G":
                result += current_char
                index += 1
            elif current_char == "(":
                if command[index + 1] == ")":
                    result += "o"
                    index += 2
                else:
                    result += "al"
                    index += 4
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.interpret(input_data))


if __name__ == "__main__":
    unittest.main()
