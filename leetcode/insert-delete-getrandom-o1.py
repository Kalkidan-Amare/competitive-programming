class RandomizedSet:

    def __init__(self):
        self.myset = set()  
        self.mylist = []
    def insert(self, val: int) -> bool:
        if val not in self.myset:
            self.myset.add(val)
            self.mylist.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.myset:
            self.myset.remove(val)
            self.mylist.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(self.mylist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()