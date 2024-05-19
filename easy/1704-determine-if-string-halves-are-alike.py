import re


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        delimeter = len(s) // 2
        return self.__count_vowels(s[0:delimeter]) == self.__count_vowels(s[delimeter:])

    def __count_vowels(self, s: str) -> int:
        return len(re.findall(r"a|e|i|o|u|A|E|I|O|U", s))


if __name__ == "__main__":
    for input_data, expected in (("book", True), ("textbook", False)):
        assert Solution().halvesAreAlike(input_data) == expected
