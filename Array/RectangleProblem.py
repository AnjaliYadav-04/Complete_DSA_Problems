class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        ans = 0

        for i in range(n):
            for j in range(i + 1, n):

                # overlap width
                width = min(topRight[i][0], topRight[j][0]) - max(bottomLeft[i][0], bottomLeft[j][0])

                # overlap height
                height = min(topRight[i][1], topRight[j][1]) - max(bottomLeft[i][1], bottomLeft[j][1])

                # if overlap exists
                if width > 0 and height > 0:
                    side = min(width, height)
                    ans = max(ans, side * side)

        return ans


# input
bottomLeft = [[1,1],[2,2],[3,1]]
topRight = [[3,3],[4,4],[6,6]]
obj = Solution()

print(obj.largestSquareArea(bottomLeft, topRight))
