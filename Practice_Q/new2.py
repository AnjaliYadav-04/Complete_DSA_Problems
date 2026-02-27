class Solution:
    def minOperations(self, s: str, k: int) -> int:
        zeros = s.count('0')
        n = len(s)
        
        if zeros == 0:
            return 0
        
        if k == 1:
            return zeros
        
        # Parity condition
        if k % 2 == 0 and zeros % 2 == 1:
            return -1
        
        # Minimum ops
        ops = (zeros + k - 1) // k
        
        if k > zeros:
            ops = max(ops, (k - zeros + 1) // 2)
        
        return ops
