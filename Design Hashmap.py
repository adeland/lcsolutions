class MyHashMap:
    def __init__(self):
        self.x = [None] * 1000001
        
    def put(self, key: int, value: int) -> None:
        self.x[key] = value

    def get(self, key: int) -> int:
        value = self.x[key]
        return value if value != None else -1

    def remove(self, key: int) -> None:
        self.x[key] = None

# NOT MY SOLUTION
