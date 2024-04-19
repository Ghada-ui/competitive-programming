class Page:
    def __init__(self,url):
        self.url = url
        self.next = None
        self.previous = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Page(homepage)
        self.current = self.head
        

    def visit(self, url: str) -> None:
        page = Page(url)
        self.current.next = page
        page.previous = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        i = 0
        while i < steps and self.current.previous:
            self.current = self.current.previous
            i += 1
        return self.current.url    

    def forward(self, steps: int) -> str:  
        i = 0
        while i < steps and self.current.next:
            self.current = self.current.next
            i += 1
        return self.current.url    

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)