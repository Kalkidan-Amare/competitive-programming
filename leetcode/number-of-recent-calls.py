class RecentCounter:

    def __init__(self):
        self.requests= []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        
        rangee = t - 3000
        while rangee >  self.requests[0]:
            self.requests= self.requests[1:]
        return len(self.requests)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)