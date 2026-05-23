class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        distance = len(gas)
        for i in range(distance):
            total = 0
            travel = 0
            for j in range(i, i + distance):
                idx = j % distance
                total += gas[idx] - cost[idx]    
                if total < 0:
                    break
                travel += 1
                if travel == distance:
                    return i
        return -1