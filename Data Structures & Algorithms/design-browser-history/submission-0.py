class Link:
    
    def __init__(self, url:str):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Link(homepage)

    def visit(self, url: str) -> None:
        node = Link(url)
        node.prev = self.curr
        self.curr.next = node
        self.curr = node
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev is None: return self.curr.url
            self.curr = self.curr.prev
        return self.curr.url

        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next is None: return self.curr.url
            self.curr = self.curr.next
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)