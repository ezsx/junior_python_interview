class ZigzagIterator:
    def __init__(self, v1: list[int], v2: list[int]):
        self.queue = []
        if v1:
            self.queue.append(iter(v1))
        if v2:
            self.queue.append(iter(v2))

    def next(self) -> int:
        iterator = self.queue.pop(0)
        value = next(iterator)
        if iterator:
            self.queue.append(iterator)
        return value

    def hasNext(self) -> bool:
        return len(self.queue) > 0
