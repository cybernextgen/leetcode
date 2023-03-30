import unittest

data = (("abba", "dog cat cat dog", True), ("abba", "dog cat cat fish", False))


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        words_mapping = dict()
        used_chars = set()

        for word, pattern_char in zip(words, pattern):
            if word not in words_mapping:
                if pattern_char in used_chars:
                    return False
                words_mapping[word] = pattern_char
                used_chars.add(pattern_char)
                continue
            used_pattern_char = words_mapping[word]
            if used_pattern_char != pattern_char:
                return False
        return True


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for pattern, test_string, result in data:
            self.assertEqual(result, s.wordPattern(pattern, test_string))


if __name__ == "__main__":
    unittest.main()
