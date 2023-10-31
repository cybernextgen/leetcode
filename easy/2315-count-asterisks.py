class Solution:
    def countAsterisks(self, s: str) -> int:
        result = 0
        is_pair = False
        for ch in s:
            if ch == '|':
                is_pair = not is_pair
            if ch == '*' and not is_pair:
                result += 1
        return result
