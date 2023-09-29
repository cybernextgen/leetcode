import unittest
from typing import List

data = ()


class MyHashSet:
    def __init__(self):
        self.__max_buckets = 2**15
        self.__buckets: List[List[int]] = [[]] * self.__max_buckets

    def add(self, key: int) -> None:
        bucket_index = self.__get_bucket_index(key)
        bucket = self.__buckets[bucket_index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket_index = self.__get_bucket_index(key)
        bucket = self.__buckets[bucket_index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket_index = self.__get_bucket_index(key)
        bucket = self.__buckets[bucket_index]
        if key in bucket:
            return True
        return False

    def __get_bucket_index(self, key: int) -> int:
        return key % self.__max_buckets


class TestCase(unittest.TestCase):
    def test_solution(self):
        myHashSet = MyHashSet()
        myHashSet.add(1)
        myHashSet.add(2)
        self.assertTrue(myHashSet.contains(1))
        self.assertFalse(myHashSet.contains(3))
        myHashSet.add(2)
        self.assertTrue(myHashSet.contains(2))
        myHashSet.remove(2)
        self.assertFalse(myHashSet.contains(2))


if __name__ == "__main__":
    unittest.main()
