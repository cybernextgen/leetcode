import unittest
from typing import List
from collections import deque

data = (([1, 1, 0, 0], [0, 1, 0, 1], 0), ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3))


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_deque = deque(students)
        sandwich_index = 0
        while True:
            remains = len(students_deque)
            for i in range(remains):
                student = students_deque.popleft()
                sandwich = sandwiches[sandwich_index]
                if student != sandwich:
                    students_deque.append(student)
                    continue
                sandwich_index += 1
                break
            else:
                break
        return len(students_deque)


class TestCase(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        for students, sandwiches, expected in data:
            self.assertEqual(s.countStudents(students, sandwiches), expected)


if __name__ == "__main__":
    unittest.main()
