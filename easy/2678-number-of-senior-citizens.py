import unittest
from typing import List

data = (
    (
        [
            "9751302862F0693",
            "3888560693F7262",
            "5485983835F0649",
            "2580974299F6042",
            "9976672161M6561",
            "0234451011F8013",
            "4294552179O6482",
        ],
        4,
    ),
    (["7868190130M7522", "5303914400F9211", "9273338290F4010"], 2),
    (["1313579440F2036", "2921522980M5644"], 0),
)


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for d in details:
            counter += 1 if int(d[11:13]) > 60 else 0
        return counter


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for details, expected in data:
            self.assertEqual(expected, s.countSeniors(details))


if __name__ == "__main__":
    unittest.main()
