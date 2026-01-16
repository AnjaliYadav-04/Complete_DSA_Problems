from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int,
                            hFences: List[int],
                            vFences: List[int]) -> int:
        MOD = 10**9 + 7

        # Add boundary fences
        hFences.extend([1, m])
        vFences.extend([1, n])

        hFences.sort()
        vFences.sort()

        # All possible horizontal distances
        h_dist = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_dist.add(hFences[j] - hFences[i])

        # All possible vertical distances
        v_dist = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_dist.add(vFences[j] - vFences[i])

        # Find the largest common distance
        common = h_dist & v_dist
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD


# -------- TESTING IN VS CODE --------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    m = 4
    n = 3
    hFences = [2, 3]
    vFences = [2]
    print(sol.maximizeSquareArea(m, n, hFences, vFences))  # Expected: 4

    # Example 2
    m = 6
    n = 7
    hFences = [2]
    vFences = [4]
    print(sol.maximizeSquareArea(m, n, hFences, vFences))  # Expected: -1
