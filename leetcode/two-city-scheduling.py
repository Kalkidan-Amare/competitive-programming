class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # sum = 0
        # for i in range(len(costs)):
        #     sum += min(costs[i])
        costs.sort(key=lambda x:x[0]-x[1])
        # suma += costs[i][0] for i in range(len(costs)//2)
        suma = sum(cost[0] for cost in costs[:len(costs)//2])
        sumb = sum(cost[1] for cost in costs[len(costs)//2:])
        return suma + sumb
