class Twitter:

    def __init__(self):
        self.cols = defaultdict(list)
        self.follows = defaultdict(set)
        self.time = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1
        self.cols[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for t in self.cols[userId]:
            tweets.append(t)
        # Include followees' tweets
        for followeeId in self.follows[userId]:
            if followeeId != userId:   # ignore self-follow
                for t in self.cols[followeeId]:
                    tweets.append(t)
        
        max_heap = [(-t,v) for (t,v) in tweets]
        heapq.heapify(max_heap)
        most_10  = [] 
        for i in range(10):
            if not max_heap:
                break
            t, tweetId = heapq.heappop(max_heap)
            most_10.append(tweetId)
        return most_10

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

