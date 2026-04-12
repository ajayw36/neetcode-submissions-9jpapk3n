from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list) # user -> list of (time, tweet_id)
        self.follow_map = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for tweet in self.tweet_map[userId]:
            heapq.heappush(heap, tweet)
            if len(heap) > 10:
                heapq.heappop(heap)
        for user in self.follow_map[userId]:
            for tweet in self.tweet_map[user]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
