import unittest

data = (
    ("capiTalIze tHe titLe", "Capitalize The Title"),
    ("First leTTeR of EACH Word", "First Letter of Each Word"),
    ("i lOve leetcode", "i Love Leetcode"),
)


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        return " ".join(
            w.capitalize() if len(w) > 2 else w for w in title.lower().split()
        )


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for input_data, expected in data:
            self.assertEqual(expected, s.capitalizeTitle(input_data))


if __name__ == "__main__":
    unittest.main()
