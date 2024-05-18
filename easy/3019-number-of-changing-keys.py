from typing import List


class Solution:
    def countKeyChanges(self, s: str) -> int:
        if not s:
            return 0

        result = 0
        prev_ch = s[0].lower()
        for ch in s.lower():
            if prev_ch != ch:
                result += 1
            prev_ch = ch
        return result


if __name__ == "__main__":
    for input_data, expexted in (("aAbBcC", 2), ("AaAaAaaA", 0)):
        assert Solution().countKeyChanges(input_data) == expexted
