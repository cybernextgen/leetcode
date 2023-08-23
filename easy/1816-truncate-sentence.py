import unittest

data = (
    ("Hello how are you Contestant", 4, "Hello how are you"),
    ("What is the solution to this problem", 4, "What is the solution"),
    ("chopper is not a tanuki", 5, "chopper is not a tanuki"),
)


class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        if not k:
            return ""

        current_words_count = 0
        for index, char in enumerate(s):
            if char == " ":
                current_words_count += 1
                if current_words_count == k:
                    return s[:index]
        return s


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, k, expected in data:
            self.assertEqual(expected, s.truncateSentence(input_data, k))


if __name__ == "__main__":
    unittest.main()
