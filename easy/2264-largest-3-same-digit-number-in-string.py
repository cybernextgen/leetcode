class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_char = ''
        for match in re.finditer(r"(?:(\d)\1{2,})", num):
            found_char = match.group(1)
            if found_char > max_char:
                max_char = found_char
        return max_char * 3
