from queue import Queue
class MyStack:
    def __init__(self):
        self.q = Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        
        left = 0
        right = self.q.qsize() - 1
        while left < right:
            self.q.queue[left], self.q.queue[right] = self.q.queue[right], self.q.queue[left]
            left += 1
            right -= 1
        ans = self.q.get()
        left = 0
        right = self.q.qsize() - 1
        while left < right:
            self.q.queue[left], self.q.queue[right] = self.q.queue[right], self.q.queue[left]
            left += 1
            right -= 1
        return ans

    def top(self) -> int:
        return self.q.queue[self.q.qsize() - 1]

    def empty(self) -> bool:
        return self.q.qsize() == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()