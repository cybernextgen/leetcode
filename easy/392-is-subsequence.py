import unittest

data = (("abc", "ahbgdc", True), ("axc", "ahbgdc", False))


class Solution:
    def isSubsequence(self, subsequence: str, source: str) -> bool:
        if not subsequence:
            return True
        subsequence_index = 0
        subsequence_len = len(subsequence)
        for source_index, source_char in enumerate(source):
            subsequence_char = subsequence[subsequence_index]
            if subsequence_char == source_char:
                subsequence_index += 1
                if subsequence_index == subsequence_len:
                    return True
        return False


class Test(unittest.TestCase):
    def test_parse(self):
        s = Solution()

        for str1, str2, result in data:
            self.assertEqual(s.isSubsequence(str1, str2), result)


if __name__ == "__main__":
    unittest.main()
