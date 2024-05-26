from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(
            abs(seat - student)
            for seat, student in zip(sorted(seats), sorted(students))
        )


if __name__ == "__main__":
    for seats, students, expected in (
        ([3, 1, 5], [2, 7, 4], 4),
        ([4, 1, 5, 9], [1, 3, 2, 6], 7),
    ):
        assert Solution().minMovesToSeat(seats, students) == expected
