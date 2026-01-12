class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # DP table
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Handle empty string with patterns like a*, a*b*, etc.
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Direct match or '.'
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]

                # '*'
                elif p[j - 1] == '*':
                    # Case 1: ignore previous char
                    dp[i][j] = dp[i][j - 2]

                    # Case 2: use previous char if it matches
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]



if __name__ == "__main__":
    sol = Solution()

    print(sol.isMatch("aa", "a"))     # False
    print(sol.isMatch("aa", "a*"))    # True
    print(sol.isMatch("ab", ".*"))    # True
    print(sol.isMatch("aab", "c*a*b"))# True
    print(sol.isMatch("mississippi", "mis*is*p*."))  # False
