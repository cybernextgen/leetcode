class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col_is_even = (ord(coordinates[0]) - 96) % 2 == 0
        if int(coordinates[1]) % 2 == 0:
            return not col_is_even
        return col_is_even
