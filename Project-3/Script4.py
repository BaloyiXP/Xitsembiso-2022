class BrowserHistory:
    def __init__(self, homepage: str):
        self.history=[homepage]
        self.i=0

    def visit(self, url: str) -> None:
        d=self.i
        d+=1
        del self.history[d:]
        self.history.append(url)
        self.i+=1

    def back(self, steps: int) -> str:
        while self.i!=0 and steps:
            self.i-=1
            steps-=1
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        while self.i!=len(self.history)-1 and steps:
            steps-=1
            self.i +=1
        return self.history[self.i]



      
homepage="BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"
url=["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]
