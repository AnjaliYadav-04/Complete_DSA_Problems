from collections import defaultdict
import heapq

class AuctionSystem:
    def __init__(self):
        # For each itemId, store bids by userId
        self.itemBids = defaultdict(dict)
        # For each itemId, maintain a max-heap of (-bidAmount, -userId)
        self.itemHeap = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        # Add or update bid
        self.itemBids[itemId][userId] = bidAmount
        heapq.heappush(self.itemHeap[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        # Update bid
        self.itemBids[itemId][userId] = newAmount
        heapq.heappush(self.itemHeap[itemId], (-newAmount, -userId))

    def removeBid(self, userId: int, itemId: int) -> None:
        # Remove bid
        if userId in self.itemBids[itemId]:
            del self.itemBids[itemId][userId]
        # Note: lazy deletion in heap → actual removal happens in getHighestBidder

    def getHighestBidder(self, itemId: int) -> int:
        if itemId not in self.itemBids or not self.itemBids[itemId]:
            return -1
        
        heap = self.itemHeap[itemId]
        bids = self.itemBids[itemId]

        # Clean up invalid heap entries
        while heap:
            bidAmount, userId = heap[0]
            bidAmount, userId = -bidAmount, -userId
            if userId in bids and bids[userId] == bidAmount:
                return userId
            else:
                heapq.heappop(heap)  # remove outdated bid

        return -1
auction = AuctionSystem()
auction.addBid(1, 7, 5)
auction.addBid(2, 7, 6)
print(auction.getHighestBidder(7))  # 2
auction.updateBid(1, 7, 8)
print(auction.getHighestBidder(7))  # 1
auction.removeBid(2, 7)
print(auction.getHighestBidder(7))  # 1
print(auction.getHighestBidder(3))  # -1
