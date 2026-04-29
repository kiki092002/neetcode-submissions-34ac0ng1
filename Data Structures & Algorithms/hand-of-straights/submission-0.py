class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize !=0:
            return False

        count = Counter(hand)
        heap = list(count.keys())
        heapq.heapify(heap)
        while heap:
            smallest = heap[0]
            for card in range(smallest,smallest+groupSize):
                if card not in count:
                    return False
                count[card]-=1
                if count[card] ==0:
                    if card!=heap[0]: 
                        return False
                    heapq.heappop(heap)
        return True

# hand = [1,1,2,3] group Size = 3
# count = {1:2,2:1,3:1}
# heap = [1,2,3]
# round 1: smallest = 1
# need = [1,2,3]
# count[1] -=1 -> 1 not 0, keep
# count[2] -=1 -> 0 card = 2 heap[0] = 1 2!=1 return False
# hand=[1,2,3,3,4,5]  groupSize=3

# count={1:1, 2:1, 3:2, 4:1, 5:1}
# heap=[1,2,3,4,5]
# round 1 smallest 1
# need [1,2,3]
# count[1] -=1 -> 0 card = heap[0] -> pop [2,3,4,5]
# count[2] -=1 -> 0 card = heap[0] -> pop [3,4,5]
# count[3] -=1 -> 1 keep heap=[3,4,5]
# round 2 smalesr = 3 need [3,4,5]
# count[3] -=1 -> 0 card = 3 pop heap [4,5]
# count[4] -= 0 pop heap [5]
# count[5] -=1 -> 0 heap [] 
# heap empty -> return True