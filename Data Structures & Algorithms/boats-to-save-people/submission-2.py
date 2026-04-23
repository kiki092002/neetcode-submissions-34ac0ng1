class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # each boat can have 1 or 2 people
        # no one is resued
        # try all possible pair (no dup)
        # count boat and take min 
        # used = [False]*len(people)
        # boats = 0
        # for i in range(len(people)):
        #     if used[i]:
        #         continue
        #     paired = False
        #     for j in range(i+1,len(people)):
        #         if people[i]+people[j] <= limit and not used[j]:
        #             used[i] = True
        #             used[j] = True
        #             boats+=1
        #             paired = True
        #             break
        #     if not paired: # not pair found and i go alon 
        #         used[i] = True
        #         boats+=1
           

        # return boats
        # find heaviest person and pair with smallest person
        # if fit -> 1 boat
        # if not heaviest goes alon 
        # sort arr 
        people.sort()
        boats = 0
        l,r = 0,len(people)-1
        while l <= r:
            if people[l]+people[r] <=limit:
                
                l+=1
            r-=1
            boats+=1
        return boats

        # # [5,1,4,2]
        # # [1,2,4,5]
        #      l r 
        # #[1,2,2,3,3] limit = 3
        #   l r

           

