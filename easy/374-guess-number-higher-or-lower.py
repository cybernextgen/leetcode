def guess(num: int) -> int:
    if num > 2:
        return -1
    elif num < 2:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left_element = 1
        right_element = n
        while True:
            medium_element = left_element + (right_element - left_element) // 2
            current_guess = guess(medium_element)
            if current_guess > 0:
                left_element = medium_element + 1
            elif current_guess < 0:
                right_element = medium_element - 1
            else:
                return medium_element


if __name__ == "__main__":
    s = Solution()
    assert s.guessNumber(2) == 2
