class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pay=[0]*len(cost)
        pay[0]=cost[0]
        pay[1]=cost[1]

        for i in range(2,len(cost)):
            pay[i]=cost[i]+min(pay[i-1],pay[i-2])
        return min(pay[-1],pay[-2])





        