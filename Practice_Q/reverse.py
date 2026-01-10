class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer limits
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648

        rev = 0  # This will store the reversed number
        sign = 1 if x >= 0 else -1  # Store the sign
        x = abs(x)  # Work with positive number for simplicity

        while x != 0:
            pop = x % 10  # Get the last digit
            x = x // 10   # Remove the last digit from x

            # Overflow check: Before multiplying by 10
            if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and pop > 7):
                return 0  # Return 0 if overflow occurs

            rev = rev * 10 + pop  # Add the digit to the reversed number

        return sign * rev  # Multiply by the original sign
