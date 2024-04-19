class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s, s[1:]))


if __name__ == "__main__":
    s = Solution()

    for input_data, expected in (("hello", 13), ("zaz", 50)):
        assert s.scoreOfString(input_data) == expected
