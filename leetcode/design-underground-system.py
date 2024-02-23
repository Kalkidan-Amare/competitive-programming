class UndergroundSystem:

    def __init__(self):
        self.inDict=defaultdict(tuple)
        self.outDict=defaultdict(lambda : defaultdict(tuple))
        #self.outDict={{}}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.inDict[id] = (stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startS,t1 =self.inDict[id]
        #self.outDict[id] = (stationName,t)
        if startS in self.outDict and stationName in self.outDict[startS]:
            prev,count = self.outDict[startS][stationName]
            self.outDict[startS][stationName] = (prev + (t - t1), count + 1)
        else:
           self.outDict[startS][stationName] = (t - t1, 1) 

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return self.outDict[startStation][endStation][0] / self.outDict[startStation][endStation][1]
        
        # total = count = 0
        # for key,value in self.inDict.items():
        #     if startStation == value[0] and key in self.outDict and self.outDict[key][0] == endStation:
        #         total = total + (self.outDict[key][1] - value[1])
        #         count += 1
        # return total/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)