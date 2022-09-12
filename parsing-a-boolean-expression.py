from typing import Dict, Iterator, List
import unittest
import re

data = [
    ("t", True),
    ("f", False),
    ("!(t)", False),
    ("!(f)", True),
    ("|(t,f)", True),
    ("&(t,f)", False),
    ("|(&(t,f,t),!(t))", False),
    ("|(f,&(t,t))", True),
    ("|(f,t)", True),
]


class Solution:
    operator_regex = re.compile(r"((?P<operator>[!&|])\((?P<arguments>.*)\))")

    def parseBoolExpr(self, expression: str) -> bool:
        search_result = self.operator_regex.search(expression)

        if search_result:
            operator = search_result.group("operator")
            arguments = self.__parse_arguments(search_result.group("arguments"))

            if operator == "|":
                for arg in arguments:
                    if self.parseBoolExpr(arg):
                        return True
                return False

            elif operator == "&":
                for arg in arguments:
                    if not self.parseBoolExpr(arg):
                        return False
                return True

            return not self.parseBoolExpr(next(arguments))
        else:
            return expression == "t"

    def __parse_arguments(self, arguments_string: str) -> Iterator[str]:
        start_index = 0
        braces_count = 0
        current_index = 0
        for current_char in arguments_string:
            current_index += 1
            if current_char == "(":
                braces_count += 1
                continue

            if current_char == ")":
                braces_count -= 1
                continue

            if current_char == "," and braces_count == 0:
                yield arguments_string[start_index : current_index - 1]
                start_index = current_index

        yield arguments_string[start_index : len(arguments_string)]


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for e, result in data:
            self.assertEqual(s.parseBoolExpr(e), result, e)


if __name__ == "__main__":
    unittest.main()
