class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for car in range(len(position)):
            arrivalTime = (target-position[car])/speed[car]
            cars.append((position[car],arrivalTime))

        cars.sort(reverse=True)

        fleet = 0 
        slow = 0
        for pos,time in cars:
            if time > slow:
                fleet+=1
                slow=time
            # do nothing

        return fleet
        #{0:3,1:2}
# speed = dis/time
# n cars on one-lane
# each car : start at some position[i] miles and drives at a constant speed[i]
# target is a fixed location head

#no passing allowed: if a faster car behind catch up slower car ahead, cannot pass
# instead join and match slowed car speed
# becom fleet
# fleet : group of car that stitch together all way to target
# singcar is fleet

# arrive time = (target - pos[i])/speed
# time 0 : 10-1/3 = 3
# time 1: 10-4/2 = 6/2 = 3
