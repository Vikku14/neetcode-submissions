class MyStack:

    def __init__(self):
        self.q = []
        

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        n = len(self.q) - 1
        for i in range(n):
            self.q.append(self.q[0])
            self.q.pop(0)
        p = self.q.pop(0)
        return p

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return not bool(len(self.q))
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()