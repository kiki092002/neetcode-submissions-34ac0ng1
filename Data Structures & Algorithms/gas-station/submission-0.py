class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost)<0:
            return -1
        tank = 0 
        start = 0 
        for i in range(len(gas)):
            tank += gas[i]-cost[i]
            print(tank,start,i)
            if tank <0:
                start = i+1
                tank = 0 
        return start
        # gas = [2,3,4]
        # cost=[3,4,3]
        # diff= [-1,-1,1] sum = -1 impossible return -1
        # gas = [1,2,3,4], cost = [2,2,4,1]
        # diff = [-1,0,-1,3] -> sum = 1
        # sum(diff) <0 -> return -1
        # if starting station i and tank goes neg at station j , can station
        # i+1 , i+2,... j be a valid start? no , skipp all and try starting at j+1

        # if tank goes neg at j: start fresh from j +1 reset tank to 0 
        # if sum(diff) >=0: a valid start always exists, its whereever we last reset

        # gas = [1,2,3,4,5]
        # cost= [3,4,5,1,2]
        # diff= [-2,-2,-2,3,3] sum = 0 possible
        # tank  =0, start = 0
        # i = 0 tank = (0-2) = -2 neg start = 1 tank = 0
        # i = 1 tank = 0-2 = -2 neg start = 2 tank 0 
        # i = 2 tank = -2 neg start = 3 tank 0
        # i = 3 tank = 3 -> ok
        # i = 4 tank = 3+3-> ok
        # answer = start

