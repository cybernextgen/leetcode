class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ""
        raw_str = s.replace('-', '').upper()
        len_raw_str = len(raw_str)
        for index, ch in enumerate(reversed(raw_str)):
            res = ch + res
            index_inc = index + 1
            if not index_inc % k and index_inc < len_raw_str:
                res = "-" + res
        return res
