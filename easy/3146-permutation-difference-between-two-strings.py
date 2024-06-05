class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        t_char_indexes = {ch: i for i, ch in enumerate(t)}
        return sum(abs(i - t_char_indexes[ch]) for i, ch in enumerate(s))


if __name__ == "__main__":
    for s, t, expected in (("abc", "bac", 2), ("abcde", "edbac", 12)):
        assert Solution().findPermutationDifference(s, t) == expected
