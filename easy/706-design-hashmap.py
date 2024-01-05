class MyHashMap:
    
  def __init__(self):
        self.backets = [None] * (10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.backets[key] = value

    def get(self, key: int) -> int:
        val = self.backets[key]
        return val if val is not None else -1

    def remove(self, key: int) -> None:
        self.backets[key] = None
