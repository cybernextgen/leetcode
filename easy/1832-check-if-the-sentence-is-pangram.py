from typing import List


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


if __name__ == "__main__":
    for input_data, expected in (
        ("thequickbrownfoxjumpsoverthelazydog", True),
        ("leetcode", False),
    ):
        assert Solution().checkIfPangram(input_data) == expected
