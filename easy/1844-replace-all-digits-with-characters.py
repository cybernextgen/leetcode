class Solution:
    def replaceDigits(self, s: str) -> str:
        result = list(s)
        for index in range(1, len(s), 2):
            old_ch = s[index - 1]
            shifts = int(s[index])
            result[index] = chr(ord(old_ch) + shifts)
        return "".join(result)
