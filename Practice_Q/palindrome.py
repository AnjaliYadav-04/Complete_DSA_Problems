class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        # Numbers ending with 0 are not palindromes unless the number is 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # For even length numbers: x == reversed_half
        # For odd length numbers: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10


# Test the solution
sol = Solution()
test_cases = [121, -121, 10, 12321, 0]
for num in test_cases:
    print(f"{num} -> {sol.isPalindrome(num)}")
