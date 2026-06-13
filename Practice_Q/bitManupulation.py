class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0
        n = len(s)
        
        # Traverse from the least significant bit to the second most significant
        for i in range(n - 1, 0, -1):
            bit = int(s[i])
            if (bit + carry) % 2 == 0:
                # Even → divide by 2
                steps += 1
            else:
                # Odd → add 1 (carry may propagate)
                steps += 2
                carry = 1
        
        # Add final step if there is a carry at the most significant bit
        steps += carry
        return steps
