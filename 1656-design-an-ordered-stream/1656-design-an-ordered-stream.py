class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.data = [None] * (n + 1)
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey] = value
        result = []
        while self.pointer <= self.n and self.data[self.pointer] is not None:
            result.append(self.data[self.pointer])
            self.pointer += 1
        return result
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)