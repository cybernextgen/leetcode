import unittest

data = (("10#11#12", "jkab"), ("1326#", "acz"))


class Solution:
    def freqAlphabets(self, s: str) -> str:
        if not s:
            return ""

        index = 0
        result = ""

        def get_char(index) -> str:
            try:
                return s[index]
            except IndexError:
                return ""

        while index < len(s):
            ch1 = s[index]
            ch2 = get_char(index + 1)
            ch3 = get_char(index + 2)

            if ch3 == "#":
                decoded_char = chr(96 + int(ch1 + ch2))
                index += 3
            else:
                decoded_char = chr(96 + int(ch1))
                index += 1
            result += decoded_char
        return result


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for coded, expected in data:
            self.assertEqual(expected, s.freqAlphabets(coded))


if __name__ == "__main__":
    unittest.main()
