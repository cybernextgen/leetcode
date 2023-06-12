import unittest
import collections
import functools

data = (
    ("balon", 0),
    ("nlaebolko", 1),
    ("loonbalxballpoon", 2),
    ("leetcode", 0),
)


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        if not text:
            return 0

        allowed_chars = {"b", "a", "l", "o", "n"}
        filtered_text = filter(lambda x: x in allowed_chars, text)
        counts = collections.Counter(filtered_text)
        if len(counts.keys()) < 5:
            return 0
        words_count = counts.most_common(1)[0][1]
        for char, count in counts.items():
            if char == "l" or char == "o":
                current_words_count = count // 2
            else:
                current_words_count = count
            if current_words_count < words_count:
                words_count = current_words_count
        return words_count


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(s.maxNumberOfBalloons(input_data), expected)


if __name__ == "__main__":
    unittest.main()
